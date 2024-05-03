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

for i in range(count_of_candidates):
    name = input("Ingrese el nombre del candidato: ")
    total_votes = 0
    count_of_provinces = int(input("Ingrese la cantidad de provincias: "))
    provinces_votes = []
    for j in range(count_of_provinces):
        province_name = input("Ingrese el nombre de la provincia: ")
        votes = int(input(f"Ingrese la cantidad de votos para {province_name}: "))
        provinces_votes.append((province_name, votes))
        total_votes += votes
    list_candidates.append((name, provinces_votes))

for candidate in list_candidates:
    name = candidate[0]
    total_votes = sum(votes for (_, votes) in candidate[1])
    print(f"El candidato {name} tiene {total_votes} votos en total.")