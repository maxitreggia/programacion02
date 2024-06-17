# 15- Realizar un generador de Múltiplos de 5


def five_multiple(number):
    for i in range(1, number + 1):
        yield i * 5


multiples = list(five_multiple(10))
print(multiples)
