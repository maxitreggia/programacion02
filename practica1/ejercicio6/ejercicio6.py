n = int(input("Ingrese una edad: "))

if n <= 0:
    print("Ingrese una edad válida")
elif n < 18:
    print("Es menor de edad")
elif n >= 18:
    print("Es mayor de edad")
