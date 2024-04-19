# Se debe crear y cargar una lista donde almacenar n sueldos. Ordenar de menor a mayor
# la lista Mostrar ordenada e informar cuantos sueldos > 25000 hay. Usar el algoritmo de
# ordenamiento.

salary_count = int(input("ingrese la cantidad de salarios a analizar: "))
list_salary = []
salary_higher = 0

for i in range(salary_count):
    list_salary.append(int(input(f"Ingrese el salario {i+1}/{salary_count}: ")))
    if list_salary[i] > 25000:
        salary_higher += 1

for i in range(salary_count):
    for j in range(salary_count - 1 - i):
        if list_salary[j] > list_salary[j+1]:
            aux = list_salary[j]
            list_salary[j] = list_salary[j+1]
            list_salary[j+1] = aux

sorted_list = sorted(list_salary)

print(f"Lista ordenada por sorted: {sorted_list}")
print(f"Lista ordenada por algoritmo: {list_salary}")
print(f"Salarios mayores a $25.000: {salary_higher}")
