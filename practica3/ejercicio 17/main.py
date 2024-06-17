from ejercicio17 import open_paint, open_calculator, create_directory, change_directory


def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Crear carpeta")
        print("2. Cambiar de carpeta")
        print("3. Abrir Paint")
        print("4. Abrir Calculadora")
        print("5. Salir")

        choice = int(input("Ingrese su opción: "))

        match choice:
            case 1:
                name = input("Ingrese el nombre de la carpeta: ")
                create_directory(name)
            case 2:
                path = input("Ingrese el camino de la carpeta: ")
                change_directory(path)
            case 3:
                open_paint()
            case 4:
                open_calculator()
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
