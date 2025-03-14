# Import required dependencies
from langgraph.graph import Graph, END, StateGraph
from typing import TypedDict

import app.Nodes as Nodes

class AgentState(TypedDict):
    messages: list[str]
    email: str
    query: str
    category: str
    booking_info: list[str]

class AgentsController:

    def where_to_go(self, state):
        cat = state['category']
        if cat == "email_query":
            return "email"
        if cat == "booking_request":
            return "booking"
        else:
            return "reply"
        
    def run(self, query):
        workflow = StateGraph(AgentState)
        entryNode = Nodes.EntryNode()
        replyNode = Nodes.ReplyNode()
        writerNode = Nodes.WriterNode()
        validateBookingNode = Nodes.ValidateBookingNode()

        workflow.add_node('entryNode',entryNode.run)
        workflow.add_node("responder", replyNode.run)
        workflow.add_node('emailNode',writerNode.run)
        workflow.add_node('validateBookingNode',validateBookingNode.run)

        workflow.add_conditional_edges('entryNode', self.where_to_go,{
            "email": "emailNode",
            "reply": "responder",
            "booking": "validateBookingNode"
        })

        workflow.add_edge("responder",END)
        workflow.add_edge("emailNode",END)
        workflow.add_edge("validateBookingNode",END)

        workflow.set_entry_point("entryNode")
        app = workflow.compile()

        inputs = {"query": query, "messages": [query]}
        result = app.invoke(inputs)

        return str(result['messages'][-1])
        #return {"response": result["messages"][-1] if "messages" in result else ""}



    