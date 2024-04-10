n = int(input("Ingrese la cantidad de sueldos a analizar:"))
sueldos = []
sueldos_mayor_300 = 0
sueldos_menor_300 = 0

for i in range(n):
    sueldos.append(int(input(f"Ingrese el sueldo del empleado {i + 1}: ")))
    if sueldos[i] > 300:
        sueldos_mayor_300 += 1
    elif sueldos[i] < 300:
        sueldos_menor_300 += 1

sum_sueldos = sum(sueldos)
print(f"El total del costo en perosonal es de: {sum_sueldos}")
print(f"Los sueldos mayores a $300 son: {sueldos_mayor_300}")
print(f"Los sueldos menores a $300 sin: {sueldos_menor_300}")
