from fecha import Fecha, DateError


def main():
    try:
        fecha_invalida = Fecha(31, 2, 2015)
    except DateError as e:
        print(f"Error: {e}")

    try:
        fecha = Fecha(28, 2, 2020)
        print(f"Fecha creada: {fecha}")
        fecha.setDia(35)
    except DateError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
