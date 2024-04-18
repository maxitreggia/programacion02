# Realizar la carga de valores enteros por teclado, almacenarlos en una lista.
# Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de
# la lista.

list_integers = []

while True:
    value = input("Ingrese numeros enteros(ingrese 0 para finalizar): ")

    try:
        number = int(value)
    except ValueError:
        print("Error: Ingrese solo numeros enteros")
        continue

    if number == 0:
        break
    list_integers.append(number)

print(f"Lista de numeros: {list_integers}")
print(f"Tamaño de la lista de numeros: {len(list_integers)}")
