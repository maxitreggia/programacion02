# Crear una lista y almacenar los nombres de n ciudades por teclado. Luego permitir ingresar
# el nombre de una ciudad y mostrar en qué posición de la lista se encuentra en caso de no
# encontrarse mostrar un mensaje.

cities = int(input("Ingrese la cantidad de ciudades: "))
list_cities = []

for i in range(cities):
    list_cities.append(input(f"Ingrese la ciudad{i + 1}/{cities}: ").upper())


print(f"La lista de ciudades es: {list_cities}")
