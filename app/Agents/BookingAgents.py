from crewai import Agent
from app.Tools import BookingTools
class BookingAgents:
    @staticmethod
    def getBookingInfoAgent():
        return Agent(
            role='Flight reservation Information Specialist',
            goal='You will receive a booking code and a user\'s last name. Your task is to manage the changes the user is asking and respond with the new information about the booking. all the responses must be in spanish',
            backstory='An expert in retrieving booking information with extensive experience in handling various booking systems.',
            tools = [BookingTools.booking_info_tool],
            verbose=True,
            allow_delegation=False,
        )
    # @staticmethod
    # def weatherAgent():
    #     return Agent(
    #         role = 'Weather Expert',
    #         goal = 'You will be given a location name and you have to find the weather information about that location using the tools provided to you',
    #         backstory = "An weather expert who is expert in providing weather information about any location",
    #         tools = [Tools.weather_tool],
    #         verbose = True,
    #         allow_delegation = False,
    #     )