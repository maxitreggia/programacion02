n = int(input("Ingrese una edad: "))

if n <= 0:
    print("Ingrese una edad valida")
elif 0 < n < 17:
    print("Es menor de edad")
elif n >= 18:
    print("Es mayor de edad")
