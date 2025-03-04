from app.Nodes.iNode import iNode;

class ReplyNode(iNode):
    def run(self, state):
        query = state["query"]
        agent = self.getOpenAIInstance().invoke(f"""
            {query}
        """)
        messages = state["messages"]
        messages.append(agent.content)
        return {"messages": messages}
