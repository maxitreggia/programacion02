from programacion02.biblioteca.biblioteca import Biblioteca


def mostrar_menu():
    """Muestra el menú de opciones para el sistema de gestión de biblioteca."""
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Agregar miembro")
    print("3. Consultar estado de libros")
    print("4. Consultar estado de miembros")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Salir")
    print("--------------------------------------")


def main():
    biblioteca = Biblioteca()

    # Datos iniciales
    print("\n--- Registro de Datos Iniciales ---")
    biblioteca.agregar_libro("El Principito", "Antoine de Saint-Exupéry", "978-3-16-148410-0", 1)
    biblioteca.agregar_libro("1984", "George Orwell", "978-0-452-28423-4", 2)
    biblioteca.agregar_miembro("Juan Pérez", 1)
    biblioteca.agregar_miembro("Ana García", 2)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Agregar Libro ---")
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            ejemplar = int(input("Ejemplar: "))
            biblioteca.agregar_libro(titulo, autor, isbn, ejemplar)

        elif opcion == "2":
            print("\n--- Agregar Miembro ---")
            nombre = input("Nombre: ")
            id_miembro = int(input("ID del Miembro: "))
            biblioteca.agregar_miembro(nombre, id_miembro)

        elif opcion == "3":
            print("\n--- Estado de los Libros ---")
            biblioteca.consultar_estado_libros()

        elif opcion == "4":
            print("\n--- Estado de los Miembros ---")
            biblioteca.consultar_estado_miembros()

        elif opcion == "5":
            print("\n--- Prestar Libro ---")
            id_miembro = int(input("ID del Miembro: "))
            isbn = input("ISBN del Libro: ")
            biblioteca.prestar_libro(id_miembro, isbn)

        elif opcion == "6":
            print("\n--- Devolver Libro ---")
            id_miembro = int(input("ID del Miembro: "))
            isbn = input("ISBN del Libro: ")
            biblioteca.devolver_libro(id_miembro, isbn)

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
