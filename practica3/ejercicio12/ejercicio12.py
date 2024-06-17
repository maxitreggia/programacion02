# 12- Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios
# de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que
# finalizará el procesamiento mediante el ingreso de un nombre vacío.
# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más
# de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un
# apellido, el usuario sólo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa
# debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer
# nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo:
# Nombre: Alba María Linares
# DNI: 25834910
# Alba7258


def get_user_details(name, middle_name, surname, dni):
    user_details = {'Nombre: ': name, 'Segundo Nombre: ': middle_name, 'Apellido: ': surname, 'DNI ': dni}
    return user_details


def get_first_name(user_details):
    return user_details['Nombre: ']


def get_len_surname(user_details):
    return str(len(user_details['Apellido: ']))


def get_first_three_numbers_of_dni(user_details):
    return str(user_details['DNI '])[:3]


def get_identifier_user(user_details):
    first_name = get_first_name(user_details)
    count_surnames = get_len_surname(user_details)
    first_three_numbers = get_first_three_numbers_of_dni(user_details)
    identifier_user = f"{first_name}{count_surnames}{first_three_numbers}"
    return identifier_user


def valid_dni(dni):
    return 7 <= len(str(dni)) <= 8 and dni.isdigit()


def main():
    while True:
        print("Para salir deje el primer nombre vacío")
        input_name = input("Ingrese el primer Nombre: ").strip()
        if input_name == "":
            break
        input_middle_name = input("Ingrese el segundo Nombre: ").strip()
        input_surname = input("Ingrese el apellido: ").strip()
        input_dni = input("Ingrese el DNI: ").strip()
        while not valid_dni(input_dni):
            print("DNI inválido. Intente nuevamente.")
            input_dni = input("Ingrese el DNI (7 u 8 dígitos): ").strip()

        user_details = get_user_details(input_name, input_middle_name, input_surname, input_dni)
        user_identifier = get_identifier_user(user_details)
        print(f"El identificador del usuario es: {user_identifier}")
        print(f"Todos los datos del usuario: {user_details}")


if __name__ == '__main__':
    main()
