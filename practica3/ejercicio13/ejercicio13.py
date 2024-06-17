# 13- Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera letra de cada
# palabra a mayúscula y las demás letras a minúscula, dejando inalterados los demás caracteres.
# Precondición: el separador de palabras es el espacio: " ". Agregar doctests con suficientes casos
# de prueba para validar que la función retorna el valor esperado ante distintos argumentos.


def titulo(text):
    """

    >>> titulo('HolA')
    'Hola'
    >>> titulo('STAR WARS')
    'Star Wars'
    >>> titulo('QUE PasO Ayer?')
    'Que Paso Ayer?'

    """
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
