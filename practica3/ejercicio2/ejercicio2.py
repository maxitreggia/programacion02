# ¿Qué sucede si los nombres de los
# parámetros dentro de la función se cambian y
# se utilizan los nombres a y b en lugar de x e
# y.

def coordenadaz(x, y):
    x = x + 10
    y = y + 15
    return x + y

# programa principal


x = int(input("Coordenada eje x: "))
y = int(input("Coordenada eje y: "))

for i in range(3):
    z = coordenadaz(x, y)
    x = x + 1
    y = y + 1
print(x, ". ", y)


# Si cambiamos los nombres de los parametros dentro de la funcion coordenadaz por a y b, el codigo seguira funcionando
# debido a que estan dentro la funcion, es decir son variable locales dentro de la misma
# y no afectan al programa principal
# Una variable solo está disponible dentro de la región en la que se crea. Esto se llama Scope
