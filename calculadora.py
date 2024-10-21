# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "no se puede dividir en 0."

# Menú de opciones
def menu():
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

# Lógica principal
if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Ingrese el número de la operación (1/2/3/4) o seleccione 's' para salir: ")

        if opcion == 's':
            print("Saliendo de la calculadora...")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print(f"El resultado es: {suma(num1, num2)}")
        elif opcion == '2':
            print(f"El resultado es: {resta(num1, num2)}")
        elif opcion == '3':
            print(f"El resultado es: {multiplicacion(num1, num2)}")
        elif opcion == '4':
            print(f"El resultado es: {division(num1, num2)}")
        else:
            print("Opción no válida, intente de nuevo.")
