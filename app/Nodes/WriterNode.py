from app.Nodes.iNode import iNode;
from app.Crews import EmailCrew

class WriterNode(iNode):
    def run(self, state):
        email = state["email"]
        emailCrew = EmailCrew(email)
        crewResult = emailCrew.run()
        messages = state["messages"]
        messages.append(crewResult)
        return {"messages": messages}
