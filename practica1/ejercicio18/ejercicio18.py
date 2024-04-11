max_input = 10
user_input = []


for i in range(max_input):
    try:
        num = int(input("Ingrese un número: "))
        user_input.append(num)
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue

if user_input:
    promedio = sum(user_input) / len(user_input)
    print(f"El promedio es: {promedio}")
else:
    print("No se ingresaron números para calcular el promedio.")