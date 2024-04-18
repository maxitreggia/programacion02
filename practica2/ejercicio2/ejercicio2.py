# Se debe crear y cargar una lista donde almacenar n sueldos. Ordenar de menor a mayor
# la lista Mostrar ordenada e informar cuantos sueldos > 25000 hay. Usar el algoritmo de
# ordenamiento.

list_salary = [25000, 35000, 40000, 50000, 60000, 70000, 30000, 20000, 10000]

long_list = len(list_salary)
salary_higher = 0

for i in range(long_list):
    if list_salary[i] > 25000:
        salary_higher += 1
    for j in range(long_list - 1 - i):
        if list_salary[j] > list_salary[j+1]:
            aux = list_salary[j]
            list_salary[j] = list_salary[j+1]
            list_salary[j+1] = aux

sorted_list = sorted(list_salary)

print(f"Lista ordenada por sorted: {sorted_list}")
print(f"Lista ordenada por algoritmo: {list_salary}")
print(f"Salarios mayores a $25.000: {salary_higher}")