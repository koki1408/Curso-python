#ejemplo con elif
ocupacion = "nada"

if ocupacion == "estudiante":
    print("Tienes 50% de descuento")
elif ocupacion == "jubilado":
    print ("Tienes 75% de descuento")
elif ocupacion == "desempleado":
    print ("tienes un 10% de descuento")
else:
    print("debes pagar el 100%")
    