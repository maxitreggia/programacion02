n = int(input("Ingrese la cantidad alturas: "))
alturas = []

for i in range(n):
    while True:
        try:
            altura = int(input(f"Ingrese la altura {i + 1} en centímetros: "))
            if altura <= 0:
                print("Ingrese una altura mayor a cero.")
            else:
                alturas.append(altura)
                break
        except ValueError:
            print("Ingrese una altura válida (número entero).")

if alturas:
    promedio = sum(alturas) / n
    print(f"El promedio de alturas es: {promedio:.2f}")
else:
    print("No se ingresaron alturas válidas.")
