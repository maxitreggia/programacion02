for i in (1, 2, 3):
    print("hola")
    """
    Returns: hola
             hola
             hola   
    """

for i in (4, 5, 6):
    print("hola")
    """
    Returns: hola
             hola
             hola   
    """

for i in ("a", "b", "c"):
    print("hola")
    """
    Returns: hola
             hola
             hola   
    """

# El resultado en los tres bucles sera la impresion de "hola" tres veces,
# pero el valor i tomara por ejemplo el valor de "a", "b", "c"

for i in ("a", "b", "c"):
    print(f"{i} hola")
    """
    Returns: a hola
             b hola
             c hola
    """
