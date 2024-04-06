n_total = 0

for i in range(1, 13):
    n = int(input(f"{i} - Ingres un numero: "))
    n_total += n
    
promedio = n_total//12

print(f"El promedio es: {promedio}")
