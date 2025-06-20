# this is a test file 
print("calculadora")
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

while True:
    print("\nOpciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", suma(a, b))
    elif opcion == "2":
        print("Resultado:", resta(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicacion(a, b))
    elif opcion == "4":
        print("Resultado:", division(a, b))
    else:
        print("Opción no válida")