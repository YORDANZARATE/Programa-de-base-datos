import math

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

def potencia(x, y):
    return x ** y

def raiz_cuadrada(x):
    return math.sqrt(x)

def seno(x):
    return math.sin(math.radians(x))

def coseno(x):
    return math.cos(math.radians(x))

def tangente(x):
    return math.tan(math.radians(x))

def logaritmo(x):
    return math.log(x)

def main():
    while True:
        print("\nOpciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Seno")
        print("8. Coseno")
        print("9. Tangente")
        print("10. Logaritmo")
        print("11. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion in ['1', '2', '3', '4', '5']:
            x = float(input("Introduce el primer número: "))
            y = float(input("Introduce el segundo número: "))

            if opcion == '1':
                print(f"{x} + {y} = {sumar(x, y)}")
            elif opcion == '2':
                print(f"{x} - {y} = {restar(x, y)}")
            elif opcion == '3':
                print(f"{x} * {y} = {multiplicar(x, y)}")
            elif opcion == '4':
                print(f"{x} / {y} = {dividir(x, y)}")
            elif opcion == '5':
                print(f"{x} ^ {y} = {potencia(x, y)}")

        elif opcion == '6':
            x = float(input("Introduce el número: "))
            print(f"√{x} = {raiz_cuadrada(x)}")

        elif opcion in ['7', '8', '9']:
            x = float(input("Introduce el ángulo en grados: "))
            if opcion == '7':
                print(f"seno({x}) = {seno(x)}")
            elif opcion == '8':
                print(f"coseno({x}) = {coseno(x)}")
            elif opcion == '9':
                print(f"tangente({x}) = {tangente(x)}")

        elif opcion == '10':
            x = float(input("Introduce el número: "))
            print(f"log({x}) = {logaritmo(x)}")

        elif opcion == '11':
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
