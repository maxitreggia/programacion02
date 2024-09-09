from numerocomplejo import NumeroComplejo


def solicitar_complejo():
    """Solicita al usuario ingresar un número complejo."""
    while True:
        try:
            real = float(input("Ingrese la parte real: "))
            imaginario = float(input("Ingrese la parte imaginaria: "))
            return NumeroComplejo(real, imaginario)
        except ValueError as e:
            print(f"Entrada no válida: {e}")


def main():
    while True:
        print("\nCalculadora de Números Complejos")
        print("1. Sumar dos números complejos")
        print("2. Multiplicar dos números complejos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ingrese el primer número complejo:")
            complejo1 = solicitar_complejo()
            print("Ingrese el segundo número complejo:")
            complejo2 = solicitar_complejo()
            resultado = complejo1.sumar(complejo2)
            print(f"Resultado de la suma: {resultado}")

        elif opcion == "2":
            print("Ingrese el primer número complejo:")
            complejo1 = solicitar_complejo()
            print("Ingrese el segundo número complejo:")
            complejo2 = solicitar_complejo()
            resultado = complejo1.multiplicar(complejo2)
            print(f"Resultado de la multiplicación: {resultado}")

        elif opcion == "3":
            print("Saliendo de la calculadora.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
