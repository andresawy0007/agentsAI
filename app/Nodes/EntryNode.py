from app.Nodes.iNode import iNode;

class EntryNode(iNode):
    def run(self, state):
        input = state["query"]
        agent = self.getOpenAIInstance().invoke(f"""
        User input
        ---
        {input}
        ---
        You have given one user input and you have to perform actions on it based on given instructions

        Categorize the user input in below categories
        booking_request: If user want to manage its flight bookin
        email_query: If user want to generate a reply to given email
        weather_query: If user want any weather info about given location
        other: If it is any other query

        After categorizing your final RESPONSE must be in json format with these properties:
        category: category of user input
        email: If category is 'email_query' then extract the email body from user input with proper line breaks and add it here else keep it blank
        query: If category is 'weather_query' or 'other' then add the user's query here else keep it blank
        booking_info: If category is 'booking_request' then add the booking info here in an array with these values:
            booking_code: the booking code that follow this regular expression: ^[A-Z0-9]{6}$
            user_lastname: the user lastname
        """)
        response = self.buildJsonRespond(agent.content)
        return {'email': response["email"], 'query': response['query'], 'category': response['category'], "booking_info": response['booking_info']}
        pass
