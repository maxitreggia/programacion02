# Realizar la carga de valores enteros por teclado, almacenarlos en una lista.
# Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de
# la lista.

while True:
    n = int(input("Ingrese numeros enteros(ingrese 0 para finalizar): "))
    numeros_enteros = []
    for i in numeros_enteros:
        if numeros_enteros[i] != 0:
            numeros_enteros.append(n)
        else:
            break

print(f"EL total de la lista es:{len(numeros_enteros)}")
