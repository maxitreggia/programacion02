
n = int(input("Ingrese un numero del 1 al 7: "))
if 1 <= n <= 7:
    match n:
        case 1:
            print("Hoy es Domingo")
        case 2:
            print("Hoy es Lunes")
        case 3:
            print("Hoy es Martes")
        case 4:
            print("Hoy es Miércoles")
        case 5:
            print("Hoy es Jueves")
        case 6:
            print("Hoy es Viernes")
        case 7:
            print("Hoy es Sábado")
else:
    print("Ingrese un numero entre 1 y 7.")
    