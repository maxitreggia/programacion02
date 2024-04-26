# Crear y cargar dos listas con los nombres de n productos en una y sus respectivos precios
# en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al
# primer producto ingresado.

number_of_products = int(input("Ingrese la cantidad de productos: "))
list_products = []
price_products = []
higher_than_firsts = 0

for i in range(number_of_products):
    list_products.append(input(f"Ingrese el nombre del producto{i + 1}/{number_of_products}: ").upper())
    price_products.append(int((input(f"Ingrese el precio del producto{i + 1}/{number_of_products}: "))))
    if price_products[0] < price_products[i]:
        higher_than_firsts += 1

print(f"La cantidad de productos mayor al primero es: {higher_than_firsts}")
