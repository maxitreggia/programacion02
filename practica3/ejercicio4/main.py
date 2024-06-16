import ejercicio4


print(ejercicio4.hello_user("maxi"))

while True:
    try:
        side = float(input('Ingrese un numero: '))
        if side <= 0:
            print('El valor debe ser mayor a 0')

        choice = input("¿Qué desea calcular? (a) Área, (p) Perímetro, (s) Salir: ").lower()
        if choice == 'a':
            area = ejercicio4.calculate_area(side)
            print(f"El area es {area}")
        elif choice == 'p':
            perimeter = ejercicio4.calculate_perimeter(side)
            print(f"El perimetro es {perimeter}")
        elif choice == 's':
            break
        else:
            print("Opción inválida. Por favor, ingrese 'a', 'p' o 's'.")
    except ValueError:
        print('Error: Ingrese un numero valido')