# 10- Realizar un programa usando funciones que permita administrar carpetas y archivos. De acuerdo
# a la función seleccionada llamar a la función correspondiente.


import os


def create_file(name):
    try:
        file = open(name, "x")
        file.close()
        return file
    except FileExistsError:
        print(f"Error: El archivo '{name}' no se pudo crear.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def read_file(name):
    try:
        with open(name, "r") as file:
            content = file.read()
            print(content)
            return content
    except FileNotFoundError:
        print(f"Error: El archivo'{name} no se pudo leer'")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def update_file(name, modify):
    try:
        with open(name, "w") as file:
            file.write(modify)
            print(f"El archivo '{name}' se modifico con exito")
    except FileNotFoundError:
        print(f"Error: El archivo'{name} no se pudo mmodificar")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def delete_file(name):
    try:
        os.remove(name)
    except FileNotFoundError:
        print(f"Error: El archivo'{name} no se pudo encontrar")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def create_folder(name):
    try:
        os.mkdir(name)
        print(f"La carpeta '{name}' se creo con exito")
    except FileExistsError:
        print(f"Error: La carperta '{name}' no se pudo crear")
    except Exception as e:
        print(f"Error: {e}")


def read_folder(path="."):
    try:
        items = os.listdir(path)
        print(f"Archivos y Carpetas en '{path}':")
        for item in items:
            print(item)
        return items
    except FileNotFoundError:
        print(f"Error: No se pudo acceder al directorio '{path}'.")
    except Exception as e:
        print(f"Error: {e}")


def update_folder(name, new_name):
    try:
        os.rename(name, new_name)
        print(f"La carpeta '{name}' se modifico correctamente a {new_name}")
    except FileNotFoundError:
        print(f"Error: La carpeta '{name}' no se pudo modificar")
    except Exception as e:
        print(f"Error: {e}")


def delete_folder(name):
    try:
        os.rmdir(name)
        print(f"La carpeta '{name}' se borro con exito")
    except FileNotFoundError:
        print(f"Error: La carpeta '{name}' no se pudo borrar")
    except Exception as e:
        print(f"Error: {e}")


def main():
    while True:
        print("Opciones de carpeta:")
        print("1 - Crear Carpeta")
        print("2 - Mostrar Carpeta/s")
        print("3 - Modificar Carpeta")
        print("4 - Borrar Carpeta")
        print("Opciones de archivos:")
        print("5 - Crear archivo")
        print("6 - Mostrar archivo")
        print("7 - Modificar archivo")
        print("8 - Borrar archivo")
        print("9 - Salir")

        option = int(input("Ingrese una opcion: "))

        match option:
            case 1:
                name_file = input("Ingrese el nombre de la carpeta: ")
                create_folder(name_file)
            case 2:
                print(f"Archivos y carpetas {read_folder()}")
            case 3:
                name_file = input("Ingrese el nombre de la carpeta a modificar: ")
                new_name_file = input("Ingrese el nuevo nombre para la carpeta: ")
                update_folder(name_file, new_name_file)
            case 4:
                name_file = input("Ingrese el nombre de la carpeta a borrar: ")
                delete_folder(name_file)
            case 5:
                name_file = input("Ingrese el nombre del archivo a crear: ")
                create_file(name_file)
            case 6:
                name_file = input("Ingrese el nombre del archivo a mostrar: ")
                read_file(name_file)
            case 7:
                name_file = input("Ingrese el nombre del archivo a modificar: ")
                new_name_file = input("Ingrese el nuevo nombre del archivo: ")
                update_file(name_file, new_name_file)
            case 8:
                name_file = input("Ingrese el nombre del archivo a mostrar: ")
                delete_file(name_file)
            case 9:
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida")


if __name__ == "__main__":
    main()
