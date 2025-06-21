calificacion = 0

preguntas = [
    {"pregunta": "existen los peces", "respuesta_correcta": "SI"},
    {"pregunta": "existen los dragones", "respuesta_correcta": "NO"},
    {"pregunta": "existen los caracoles", "respuesta_correcta": "SI"},    
]



for pregunta in preguntas:
    respuesta = input(pregunta["pregunta"] + " (SI/NO): ").upper()
    if respuesta == pregunta["respuesta_correcta"]:
        calificacion += 1

print("Tu calificación final es:", calificacion, "de 3")
    