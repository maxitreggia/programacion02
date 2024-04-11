n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un segundo numero: "))

if n1 > n2:
    print("El primer numero ingresado es mayor")
    suma = n1 + n2
    diferencia = n1 - n2
    print(f"Resultado de la suma: {suma} \nResultado de la diferencia: {diferencia}")
elif n2 > n1:
    print("El segundo numero ingresado es mayor")
    producto = n1 * n2
    divisor = n1 / n2
    print(f"Resultado del producto: {producto} \nResultado del divisio: {divisor}")