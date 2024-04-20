# Crear dos listas paralelas y almacenar los nombres de n países y su población. Ordenar
# de mayor a menor por cantidad de habitantes la lista e imprimirla. Usar algoritmo de
# ordenamiento.

countrys = int(input("Ingrese la cantidad de ciudades: "))
list_countrys = []
population_countrys =[]

for i in range(countrys):
    list_countrys.append(input(f"Ingrese el pais{i + 1}/{countrys}: ").upper())
    population_countrys.append(int((input(f"Ingrese la poblacion del pais{i + 1}/{countrys}: "))))

for i in range(countrys):
    for j in range(0, countrys - 1 - i):
        if population_countrys[j] < population_countrys[j + 1]:
            population_countrys[j], population_countrys[j + 1] = population_countrys[j + 1], population_countrys[j]
            list_countrys[j], list_countrys[j + 1] = list_countrys[j + 1], list_countrys[j]

print("\nPaises ordenado de mayor a menor")
for list_countrys, population_countrys in zip(list_countrys, population_countrys):
    print(f"{list_countrys}: {population_countrys} habitantes")
