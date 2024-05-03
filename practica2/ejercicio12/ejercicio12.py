# Confeccionar un programa que permita cargar un código de producto como clave en un
# diccionario. Guardar para dicha clave el nombre del producto, su precio y cantidad en stock.
# Implementar las siguientes actividades:
#  Carga de datos en el diccionario.
#  Listado completo de productos.
#  Consulta de un producto por su clave, mostrar el nombre, precio y stock.
#  Listado de todos los productos que tengan un stock con valor cero.

products = {}
while True:
    code = input("Ingrese el código del producto (o escriba 'fin' para terminar): ")
    if code.lower() == "fin":
        break
    name = input(f"Ingrese el nombre del producto con código {code}: ")
    price = float(input(f"Ingrese el precio del producto {name}: "))
    stock = int(input(f"Ingrese la cantidad en stock del producto {name}: "))
    products[code] = {"nombre": name, "precio": price, "stock": stock}


print("Listado completo de productos:")
for code, product in products.items():
    print(f"Código: {code}, Nombre: {product['nombre']}, Precio: {product['precio']}, Stock: {product['stock']}")


query_key = input("Ingrese el código del producto a consultar: ")
if query_key in products:
    queried_product = products[query_key]
    print(f"Nombre: {queried_product['nombre']}, Precio: {queried_product['precio']}, Stock: {queried_product['stock']}")
else:
    print("El producto no fue encontrado.")


print("Listado de productos con stock cero:")
for code, product in products.items():
    if product["stock"] == 0:
        print(f"Código: {code}, Nombre: {product['nombre']}, Precio: {product['precio']}")
