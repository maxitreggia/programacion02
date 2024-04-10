while True:

    n = int(input("Ingrese la cantidad de notas (para terminar la ejecucion ingrese 0): "))
    notas = []
    contador_mayores = 0
    contador_menores = 0

    if n != 0:
        for i in range(n):
            notas.append(int(input("Ingrese la nota: ")))
            if notas[i] >= 7:
                contador_mayores += 1
            else:
                contador_menores += 1

        print(f"La cantidad de notas mayores es: {contador_mayores}")
        print(f"La cantidad de notas menores es: {contador_menores}")
    else:
        break
