from langchain.tools import tool

class BookingTools:
    @tool("Tool to get the booking information")
    def booking_info_tool(booking_code, user_lastname):
        """
        Use this tool when you have given a location and you want to find the weather of that location
        """
        print("booking,")
        data = "data_dummy"
        return data