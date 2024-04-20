# Crear una lista y almacenar los nombres de n ciudades por teclado. Luego permitir ingresar
# el nombre de una ciudad y mostrar en qué posición de la lista se encuentra en caso de no
# encontrarse mostrar un mensaje.

cities = int(input("Ingrese la cantidad de ciudades: "))
list_cities = []
keep = ''

for i in range(cities):
    list_cities.append(input(f"Ingrese la ciudad{i + 1}/{cities}: ").upper())

while keep != 'N':
    search_cities = input("Ingrese una ciudad que desea buscar: ").upper()

    if search_cities in list_cities:
        postion = list_cities.index(search_cities) + 1
        print(f"La ciudad {search_cities.capitalize()} se encuntra en la posicion {postion} de la lista")
    else:
        print("La ciudad no se encuentra en la lista")
    keep = input("Desea continuar? [S/N] ").upper()
