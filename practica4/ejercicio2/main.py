from numeroracional import NumeroRacional


def solicitar_racional():
    """Solicita al usuario ingresar un número racional."""
    while True:
        try:
            numerador = int(input("Ingrese el numerador: "))
            denominador = int(input("Ingrese el denominador (diferente de 0): "))
            if denominador == 0:
                raise ValueError("El denominador no puede ser cero.")
            return NumeroRacional(numerador, denominador)
        except ValueError as e:
            print(f"Entrada no válida: {e}")


def main():
    while True:
        print("\nCalculadora de Números Racionales")
        print("1. Sumar dos números racionales")
        print("2. Multiplicar dos números racionales")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ingrese el primer número racional:")
            racional1 = solicitar_racional()
            print("Ingrese el segundo número racional:")
            racional2 = solicitar_racional()
            resultado = racional1.sumar(racional2)
            print(f"Resultado de la suma: {resultado}")

        elif opcion == "2":
            print("Ingrese el primer número racional:")
            racional1 = solicitar_racional()
            print("Ingrese el segundo número racional:")
            racional2 = solicitar_racional()
            resultado = racional1.multiplicar(racional2)
            print(f"Resultado de la multiplicación: {resultado}")

        elif opcion == "3":
            print("Saliendo de la calculadora.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
