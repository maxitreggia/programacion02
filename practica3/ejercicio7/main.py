from ejercicio7 import calculate_cost

number_of_measures = 0
while number_of_measures <= 0:
    try:
        number_of_measures = int(input("Ingrese la cantidad de medidas: "))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

list_of_measures = []
for i in range(number_of_measures):
    while True:
        try:
            n = float(input(f"Ingrese la medida {i + 1}/{number_of_measures}: "))
            if n <= 0:
                raise ValueError
            list_of_measures.append(n)
            break
        except ValueError:
            print("Por favor, ingrese un número válido y positivo.")

cost_per_meter = -1
while cost_per_meter <= 0:
    try:
        cost_per_meter = float(input("Ingrese el costo por metro: "))
    except ValueError:
        print("Por favor, ingrese un número válido y positivo.")

total_cost = calculate_cost(list_of_measures, cost_per_meter)
print(f"El costo total para cercar el terreno es: {total_cost}")
