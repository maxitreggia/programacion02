# 16- Realizar un generador de números de Fibonacci

def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print([fibonacci(n) for n in range(10)])
