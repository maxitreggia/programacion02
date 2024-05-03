while True:
    username = input("Ingrese su nombre de usuario (entre 6 y 12 caracteres): ")

    if len(username) < 6 or len(username) > 12:
        print("Error: El nombre de usuario debe tener entre 6 y 12 caracteres.")
        continue

    password = input("Ingrese su contraseña (mínimo 8 caracteres, sin espacios): ")

    if len(password) < 8:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        continue
    if ' ' in password:
        print("Error: La contraseña no puede contener espacios en blanco.")
        continue

    break

print("\nCredenciales aceptadas:")
print(f"Usuario: {username}")
print(f"Contraseña: {'*' * len(password)}")
