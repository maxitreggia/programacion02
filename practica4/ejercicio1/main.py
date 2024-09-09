from programacion02.practica4.ejercicio1.punto3d import Punto3D


def solicitar_coordenada(coordenada):
    """Solicita al usuario ingresar una coordenada y valida que sea un número."""
    while True:
        try:
            valor = float(input(f"Ingrese el valor de {coordenada}: "))
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


def main():
    print("Ingrese las coordenadas para el primer punto:")
    x1 = solicitar_coordenada("x")
    y1 = solicitar_coordenada("y")
    z1 = solicitar_coordenada("z")

    print("Ingrese las coordenadas para el segundo punto:")
    x2 = solicitar_coordenada("x")
    y2 = solicitar_coordenada("y")
    z2 = solicitar_coordenada("z")

    punto1 = Punto3D(x1, y1, z1)
    punto2 = Punto3D(x2, y2, z2)

    print("\nPuntos ingresados:")
    print(punto1)
    print(punto2)


if __name__ == "__main__":
    main()

