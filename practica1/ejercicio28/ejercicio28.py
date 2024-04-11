n = int(input("Ingrese la cantidad de nombres a cargar: "))

nombres = []

for i in range(n):
    nombre = input("Ingrese el nombre {}: ".format(i + 1))
    nombres.append(nombre.upper())

for nombre in nombres:
    if nombre[0] in "AEIOU":
        print("{} comienza con vocal.".format(nombre))
