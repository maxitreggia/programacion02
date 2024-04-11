oracion = input("Ingrese una oracion oracion: ")
vacio = 0

for caracter in oracion:
    if " " in caracter:
        vacio += 1

print(f"Espacios vacios en la oracion: {vacio}")
