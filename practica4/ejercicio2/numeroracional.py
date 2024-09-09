import math


class NumeroRacional:
    def __init__(self, numerador=0, denominador=1):
        """
        Constructor que inicializa el número racional.
        Si no se proporcionan argumentos, el número racional es 0/1 por defecto.
        Si se proporciona un objeto de tipo NumeroRacional, realiza una copia.
        """
        if isinstance(numerador, NumeroRacional):
            # Constructor de copia
            self.numerador = numerador.numerador
            self.denominador = numerador.denominador
        else:
            # Constructor normal
            if denominador == 0:
                raise ValueError("El denominador no puede ser cero.")
            self.numerador = numerador
            self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        """Simplifica el número racional dividiendo por el máximo común divisor."""
        divisor_comun = math.gcd(self.numerador, self.denominador)
        self.numerador //= divisor_comun
        self.denominador //= divisor_comun

    def sumar(self, otro):
        """Suma dos números racionales y devuelve un nuevo número racional."""
        nuevo_numerador = self.numerador * otro.denominador + otro.numerador * self.denominador
        nuevo_denominador = self.denominador * otro.denominador
        return NumeroRacional(nuevo_numerador, nuevo_denominador)

    def multiplicar(self, otro):
        """Multiplica dos números racionales y devuelve un nuevo número racional."""
        nuevo_numerador = self.numerador * otro.numerador
        nuevo_denominador = self.denominador * otro.denominador
        return NumeroRacional(nuevo_numerador, nuevo_denominador)

    def __str__(self):
        """Devuelve una representación en cadena del número racional."""
        return f"{self.numerador}/{self.denominador}"
