from programacion02.facultad.facultad import Facultad


def mostrar_menu():
    print("\n--- Sistema de Gestión de Facultad ---")
    print("1. Registrar estudiante")
    print("2. Registrar curso")
    print("3. Inscribir estudiante en curso")
    print("4. Dar de baja a estudiante de curso")
    print("5. Consultar estado de cursos")
    print("6. Consultar estado de estudiantes")
    print("7. Salir")
    print("--------------------------------------")


def main():
    facultad = Facultad()

    # Datos iniciales
    print("\n--- Registro de Datos Iniciales ---")
    facultad.agregar_estudiante("Juan", "Pérez", "20230001", "Ingeniería")
    facultad.agregar_estudiante("Ana", "García", "20230002", "Matemáticas")
    facultad.agregar_estudiante("Luis", "Martínez", "20230001", "Física")  # Estudiante duplicado

    facultad.agregar_curso("Matemáticas Básicas", "MATH101", "Dr. Smith", 2)
    facultad.agregar_curso("Programación en Python", "CS101", "Prof. Johnson", 1)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Registro de Estudiante ---")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            matricula = input("Matrícula: ")
            carrera = input("Carrera: ")
            facultad.agregar_estudiante(nombre, apellido, matricula, carrera)

        elif opcion == "2":
            print("\n--- Registro de Curso ---")
            nombre_curso = input("Nombre del Curso: ")
            codigo_curso = input("Código del Curso: ")
            profesor = input("Profesor Encargado: ")
            capacidad_maxima = int(input("Capacidad Máxima: "))
            facultad.agregar_curso(nombre_curso, codigo_curso, profesor, capacidad_maxima)

        elif opcion == "3":
            print("\n--- Inscripción a Curso ---")
            estudiante_id = int(input("ID del Estudiante: "))
            codigo_curso = input("Código del Curso: ")
            facultad.inscribir_estudiante_en_curso(estudiante_id, codigo_curso)

        elif opcion == "4":
            print("\n--- Baja de Estudiante del Curso ---")
            estudiante_id = int(input("ID del Estudiante: "))
            codigo_curso = input("Código del Curso: ")
            facultad.baja_estudiante_de_curso(estudiante_id, codigo_curso)

        elif opcion == "5":
            print("\n--- Estado de los Cursos ---")
            facultad.consultar_estado_cursos()

        elif opcion == "6":
            print("\n--- Estado de los Estudiantes ---")
            facultad.consultar_estado_estudiantes()

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
