from flask import Flask, request, jsonify

from app.Controllers import AgentsController

app = Flask(__name__)

@app.route('/talkto', methods=['POST'])
def talk_to():
    # Retrieve the 'text' parameter from the JSON body
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input, please provide "text" in the JSON body'}), 400
    
    text_value = data['text']

    agentsController = AgentsController()
    result = agentsController.run(text_value);
    # Processing can be done here with the `text_value`
    # For now, we simply return it as a response
    return jsonify({'ai_response': result})

if __name__ == '__main__':
    app.run(debug=True)
