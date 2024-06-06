# 3- Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere
# calcular y mostrar su perímetro o su superficie y en función de eso llame a la función perímetro o
# superficie. Retornar el valor calculado.


def calculate_area(side):
    return side*side


def calculate_perimeter(side):
    return side*4


while True:
    try:
        side = float(input('Ingrese un numero: '))
        if side <= 0:
            print('El valor debe ser mayor a 0')

        choice = input("¿Qué desea calcular? (a) Área, (p) Perímetro, (s) Salir: ").lower()
        if choice == 'a':
            area = calculate_area(side)
            print(f"El area es {area}")
        elif choice == 'p':
            perimeter = calculate_perimeter(side)
            print(f"El perimetro es {perimeter}")
        elif choice == 's':
            break
        else:
            print("Opción inválida. Por favor, ingrese 'a', 'p' o 's'.")
    except ValueError:
        print('Error: Ingrese un numero valido')
