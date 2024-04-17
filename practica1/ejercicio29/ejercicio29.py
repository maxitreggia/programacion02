n = int(input("Ingrese la cantidad de triángulos: "))

cantidad_equilateros = 0
cantidad_isosceles = 0
cantidad_escalenos = 0

for i in range(1, n + 1):
    print(f"Ingrese los lados del triángulo {i}:")
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))

    if lado1 == lado2 == lado3:
        tipo = "equilátero"
        cantidad_equilateros += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "isósceles"
        cantidad_isosceles += 1
    else:
        tipo = "escaleno"
        cantidad_escalenos += 1

    print(f"El triángulo {i} es {tipo}\n")

print("\nResumen:")
print(f"{cantidad_equilateros} triángulo(s) equilátero(s)")
print(f"{cantidad_isosceles} triángulo(s) isósceles(es)")
print(f"{cantidad_escalenos} triángulo(s) escaleno(s)")