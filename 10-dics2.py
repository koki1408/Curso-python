#inciar un diccionario vacio 
jugador = {}
print(jugador)

 #se une un jugador
jugador["nombre"] = "Irvin"
jugador["putaje"] = 0
print(jugador)

#incrementando el putaje
jugador["putaje"] = 100
print (jugador)

#incrementando el putaje
jugador["putaje"] = 200
print (jugador)

#Acceder a un valor
print(jugador.get("consola", "no exsiste ese valor"))

#iterar en el diccionario
for llave, valor in jugador.items():
    print(valor)

#eliminar juagador y puntaje
del jugador["nombre"]
del jugador["putaje"]
print(jugador)