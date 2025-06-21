# Creando un diccionario simple
cancion = {
     "artista": "metallica", #llave y valor
     "cancion": "Enter Sandman",
     "lanzamiento": 1992,
     "likes": 3000,        
}

#acceder a los lementos de un diccionario
print(cancion["artista"])
print(cancion["lanzamiento"])

#mezclar con un string
artista = cancion["artista"]
print(f"estoy escuchando a {artista}")

print(cancion)

#agregar nuevos valores
cancion["playlist"] = "heavy metal"
print(cancion)

#resplazar valor existente
cancion["cancion"] = "seek and destroy"
print(cancion)

#eliminar un valor
del cancion["lanzamiento"]
print(cancion)