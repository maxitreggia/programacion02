# Crear una lista y almacenar los nombres de n ciudades por teclado. Luego permitir ingresar
# el nombre de una ciudad y mostrar en qué posición de la lista se encuentra en caso de no
# encontrarse mostrar un mensaje.

cities = int(input("Ingrese la cantidad de ciudades: "))
list_cities = []
keep = ''

for i in range(cities):
    list_cities.append(input(f"Ingrese la ciudad{i + 1}/{cities}: ").upper())


print(f"La lista de ciudades es: {list_cities}")

while keep != 'N':
    search_cities = input("Ingrese una ciudad que desea buscar: ")
    if search_cities in list_cities:
        print(f"La lista de ciudades es: {list_cities}")
    else:
        print("La ciudad ingresada no se encuntra en la lista")
    keep = input("Desea continuar? [S/N] ").upper()
