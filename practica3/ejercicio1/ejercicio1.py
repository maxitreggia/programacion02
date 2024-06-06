# 1- Codificar en Python una función que calcule e imprima el promedio de tres calificaciones. Las
# calificaciones se reciben por parámetro y el promedio debe retornarse y mostrarse en el programa
# que llamó a la función.

def calculate_average():
    total = 0
    count = 0
    while count < 3:
        try:
            value = float(input(f"Ingrese un numero {count + 1}/3: "))
            total += value
            count += 1
        except ValueError:
            print("Error: ingrese un valor numerico")
    return total / 3


avarage = calculate_average()
print(f"El valor promedio es: {avarage:.2f}")
