from app.Agents import BookingAgents
from app.Tasks import BookingTasks
from crewai import Crew

class BookingCrew:
    def __init__(self, booking_info):
        self.booking_info = booking_info
    def run(self):
        # Agents
        bookingInfoAgent = BookingAgents.getBookingInfoAgent()
        # Tasks
        findBookingInformationTask = BookingTasks.findBookingInformation(agent=bookingInfoAgent, booking_code=self.booking_info["booking_code"], user_lastname=self.booking_info["user_lastname"])
        # Create crew
        crew = Crew(
            agents=[bookingInfoAgent],
            tasks=[findBookingInformationTask],
            verbose=True, # Set to True for verbose logging
        )
        # Run the crew
        result = crew.kickoff()
        return result