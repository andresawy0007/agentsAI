
# Import required dependencies
from langgraph.graph import Graph, END, StateGraph
from typing import TypedDict

import app.Nodes as Nodes




    


  

workflow = StateGraph(AgentState)
entryNode = Nodes.EntryNode()
replyNode = Nodes.ReplyNode()
writerNode = Nodes.WriterNode()
validateBookingNode = Nodes.ValidateBookingNode()

workflow.add_node('entryNode',entryNode.run)
workflow.add_node("responder", replyNode.run)
workflow.add_node('emailNode',writerNode.run)
workflow.add_node('validateBookingNode',validateBookingNode.run)

workflow.add_conditional_edges('entryNode', where_to_go,{
    "email": "emailNode",
    "reply": "responder",
    "booking": "validateBookingNode"
})

workflow.add_edge("responder",END)
workflow.add_edge("emailNode",END)
workflow.add_edge("validateBookingNode",END)

workflow.set_entry_point("entryNode")
app = workflow.compile()
query = input("Please enter your query: ")

print("User request:")
print(query)
inputs = {"query": query, "messages": [query]}
result = app.invoke(inputs)
print("Agent Response:",result['messages'][-1])