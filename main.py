
# Import required dependencies
from langgraph.graph import Graph, END, StateGraph
from typing import TypedDict

import app.Nodes as Nodes




    


  

workflow = StateGraph(AgentState)
entryNode = Nodes.EntryNode()
replyNode = Nodes.ReplyNode()
writerNode = Nodes.WriterNode()
validateBookingNode = Nodes.ValidateBookingNode()

workflow.add_node('entryNode',entryNode.run)
workflow.add_node("responder", replyNode.run)
workflow.add_node('emailNode',writerNode.run)
workflow.add_node('validateBookingNode',validateBookingNode.run)

workflow.add_conditional_edges('entryNode', where_to_go,{
    "email": "emailNode",
    "reply": "responder",
    "booking": "validateBookingNode"
})

workflow.add_edge("responder",END)
workflow.add_edge("emailNode",END)
workflow.add_edge("validateBookingNode",END)

workflow.set_entry_point("entryNode")
app = workflow.compile()

query = """
Hola. Cómo estás? Mi nombre es Andrés Guerrero y quisiera cambiar la reserva que tengo para el martes. 
Eh. Déjame ya te muestro el número de reserva. Le estoy buscando. Listo. 
reserva es KLPOW8 y era una reserva que tenía para este lunes, pero pues no puedo ir. Quisiera por favor que me ayudes cambiando la reserva. 
para el siguiente martes. Muchísimas gracias. 
"""

querys = """
Can you reply to this email

Hello,
Thank you for applying to xyz company
can you share me your previous CTC
Thanks,
HR
"""

print("User request:")
print(query)
inputs = {"query": query, "messages": [query]}
result = app.invoke(inputs)
print("Agent Response:",result['messages'][-1])