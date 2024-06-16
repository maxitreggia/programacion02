# 5- El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero
# en su lugar imprime 5. ¿Qué hay que corregir?

def maximo(a, b):
    if x > y:
        return x
    else:
        return y


def minimo(a, b):
    if x < y:
        return x
    else:
        return y


#programa principal

x = int(input("Un número: "))

y = int(input("Otro número: "))

print(maximo(x - 3, minimo(x + 2, y - 5)))


# Loa argumentos dentro de las funciones hacian referencias a las variables goblales en lugar de los
# argumentos que reciben, al cabiar 'x' por 'a' y 'y' por 'b' esto asegura que las funciones comparen los
# valores que se le pasan como argumentos y no como variables globales.
def maximo(a, b):
    if a > b:
        return a
    else:
        return b


def minimo(a, b):
    if a < b:
        return a
    else:
        return b
