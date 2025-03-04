from crewai import Task
from textwrap import dedent
class BookingTasks:
    def findBookingInformation(agent,booking_code, user_lastname):
        return Task(
            description=dedent(f"""
            Get the booking code and user last name from the user query and find the booking information about the reservation.
            here is the user query
            User last name: {user_lastname}
            booking code: {booking_code}
            """),
            agent = agent,
            expected_output = "the booking information in text format"
        )
    