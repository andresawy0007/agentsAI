from app.Nodes.iNode import iNode;
from app.Crews import BookingCrew

class ValidateBookingNode(iNode):
    def run(self, state):
        bookingCrew = BookingCrew(state["booking_info"])
        crewResult = bookingCrew.run();
        messages = state["messages"]
        messages.append(crewResult)
        return {"messages": messages}
