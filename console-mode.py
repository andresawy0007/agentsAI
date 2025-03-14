
from app.Controllers import AgentsController
from termcolor import colored
def talk_to(textInput):

    agentsController = AgentsController()
    result = agentsController.run(textInput);
    # Processing can be done here with the `text_value`
    # For now, we simply return it as a response
    print(colored("Respuesta del agente: " + result, 'yellow'))

while True:
    query = input("Mensaje: ")
    if query.lower() in ['exit', 'salir']:
        print("Adiós!")
        break
    talk_to(query)
