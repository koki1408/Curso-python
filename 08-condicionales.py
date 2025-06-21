#Revisar si una condicion es mayor a
balance = 500
if balance > 0:
    print("Puedes pagar")
else:
    print("no tiene saldo") 
    
#Likes
likes = 200
if likes >= 200:
    print("Exelente, 200 likes")
else:
    print("casi llegas a los 200")

#if con texto
lenguaje = "PHP"
if not lenguaje == "Python":
    print("Exelente decision")
  
#como evaluar un boolean
usuario_autenticado = True  

if usuario_autenticado:
    print("Acceso al sistema")
else:
    print("debes inciar sesion")
    
#evaluar un elemnto de una lista
lenguajes = ["Python", "Kotlin", "Java", "JavaScript", "PHP"]

if "PHP" in lenguajes:
    print("PHP si existe")
else:
    print("No no esta en la lista")
    
#IF anidados
usuario_autenticado = False  
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print("Acceso total")
    else:
        print ("acceso al sistema")
else:
    print("debes inciar sesion")