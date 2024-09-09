class NumeroComplejo:
    def __init__(self, real=0, imaginario=0):
        """
        Constructor que inicializa el número complejo.
        Si no se proporcionan argumentos, el número complejo es 0 + 0i por defecto.
        """
        self.real = real
        self.imaginario = imaginario

    def sumar(self, otro):
        """Suma dos números complejos y devuelve un nuevo número complejo."""
        nuevo_real = self.real + otro.real
        nuevo_imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(nuevo_real, nuevo_imaginario)

    def multiplicar(self, otro):
        """Multiplica dos números complejos y devuelve un nuevo número complejo."""
        nuevo_real = self.real * otro.real - self.imaginario * otro.imaginario
        nuevo_imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(nuevo_real, nuevo_imaginario)

    def __str__(self):
        """Devuelve una representación en cadena del número complejo."""
        signo = '+' if self.imaginario >= 0 else '-'
        return f"{self.real} {signo} {abs(self.imaginario)}i"
