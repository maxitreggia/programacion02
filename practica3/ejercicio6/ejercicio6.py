# 6- Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no
# lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígito

def is_valid_dni(dni):
    try:
        dni_int = int(dni)
    except ValueError:
        return "Ingrese un número, por favor"

    if len(str(dni)) in range(7, 9):
        return "El numero de DNI es valido"
    else:
        return "EL numero de DNI es invalido, debe contener entre 7 u 8 caracteres"


input_dni = input("Ingrese un numero de DNI: ")

print(is_valid_dni(input_dni))
