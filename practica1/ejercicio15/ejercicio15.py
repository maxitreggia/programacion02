n = int(input("Ingrese la cantidad de piezas a procesar: "))

piezas_aptas = 0

for i in range(n):
    longitud = float(input("Ingrese la longitud de la pieza {}: ".format(i + 1)))

    if 1.20 <= longitud <= 1.30:
        piezas_aptas += 1

print("Cantidad de piezas aptas:", piezas_aptas)