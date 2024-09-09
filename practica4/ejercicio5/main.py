from password import Password


def main():
    try:
        cantidad = int(input("Ingrese la cantidad de contraseñas a generar: "))
        if cantidad <= 0:
            raise ValueError("El número debe ser mayor que 0.")
    except ValueError as e:
        print(f"Entrada no válida: {e}")
        return

    passwords = []
    for i in range(cantidad):
        try:
            longitud = int(input(f"Ingrese la longitud para la contraseña {i + 1}: "))
        except ValueError:
            print("Entrada no válida. Se usará la longitud por defecto (8).")
            longitud = 8

        passwords.append(Password(longitud))

    fortalezas = [p.esFuerte() for p in passwords]

    diccionario_passwords = {p.get_contraseña(): es_fuerte for p, es_fuerte in zip(passwords, fortalezas)}

    print("\nContraseñas generadas y su fortaleza:")
    for contraseña, es_fuerte in diccionario_passwords.items():
        print(f"{contraseña} - {'Fuerte' if es_fuerte else 'Débil'}")


if __name__ == "__main__":
    main()
