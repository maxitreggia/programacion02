# Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
# En una lista cargar en la primer componente el nombre del candidato y en la segunda
# componente cargar una lista con componentes de tipo tupla con el nombre de la provincia y la
# cantidad de votos obtenidos en dicha provincia.
# Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una
# estructura similar a esta:
# candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) ,
# ("luis", [("buenos aires",20)]) ]
# - Cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
# - Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las
# provincias.

count_of_candidates = int(input("Ingrese la cantidad de candidatos: "))
list_candidates = []
total_votes = []

for i in range(count_of_candidates):
    name = input("Ingrese el nombre del candidato: ")
    total_votes = 0
    count_of_provinces = int(input("Ingrese la cantidad de provincias: "))
    for j in range(count_of_provinces):
        province_name = input("Ingrese el nombre del provincia: ")
        votes = int(input("Ingrese la cantidad de votos: "))
        list_candidates.append([province_name, votes])
        total_votes += votes

for i in range(count_of_candidates):
    print(f"El candidato , tuvo {total_votes} votos.")
