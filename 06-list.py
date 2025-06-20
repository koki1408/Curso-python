lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

print(lenguajes)

# los arrays (list) comienzan en la posicion 0
print(lenguajes[0]) #python

# 0ordenar los elementos 
lenguajes.sort()
print(lenguajes)

#Acceder a un elemnto dentro de un texto
Aprendiendo = f"Estoy aprendiendo {lenguajes [3]}"
print (Aprendiendo)

# Modificando valores de un arreglo (list)
lenguajes [2] = "PHP"
print(lenguajes)

#Agregar elementos a un arreglo (list)
lenguajes.append("Ruby")
print(lenguajes)

# eliminar de un arreglo (list)
del lenguajes [1]
print (lenguajes)

#Elimiar de un arreglo (list) con pop
lenguajes.pop() #eliminar el ultimo elemento 
print (lenguajes)

#eliminar con pop una posicion en especifico 
lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre
lenguajes.remove("PHP")
print(lenguajes)