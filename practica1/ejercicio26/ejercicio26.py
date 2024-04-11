oracion = input("Ingrese una oracion: ")

oracion = oracion.lower()
vocales = ["a", "e", "i", "o", "u"]
contador_vocales = 0

for letra in oracion:
    if letra in vocales:
        contador_vocales += 1

print(f"Cantidad de vocales: {contador_vocales}")
