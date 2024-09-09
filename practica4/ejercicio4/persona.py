from enum import Enum
import random


class Sexo(Enum):
    MUJER = "Mujer"
    HOMBRE = "Hombre"


class Persona:
    def __init__(self, nombre="", edad=0, sexo=Sexo.MUJER, peso=0.0, altura=0.0):
        """Constructor de la clase Persona. Genera un DNI automáticamente."""
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = self.__generaDNI()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    # Métodos privados
    def __generaDNI(self):
        """Genera un número aleatorio de 8 cifras para el DNI."""
        return random.randint(10000000, 99999999)

    # Métodos públicos
    def calcularIMC(self):
        """Calcula el índice de masa corporal de la persona."""
        if self.__altura > 0:
            return self.__peso / (self.__altura ** 2)
        else:
            return 0

    def valorarPesoCorporal(self):
        """Devuelve -1 si está por debajo de su peso ideal, 0 si está en su peso ideal, y 1 si tiene sobrepeso."""
        imc = self.calcularIMC()
        if imc < 18:
            return -1
        elif 18 <= imc <= 25:
            return 0
        else:
            return 1

    def esMayorDeEdad(self):
        """Indica si la persona es mayor de edad."""
        return self.__edad >= 18

    def __str__(self):
        """Devuelve toda la información de la persona como una cadena de caracteres."""
        return (f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__dni}, "
                f"Sexo: {self.__sexo.value}, Peso: {self.__peso} kg, Altura: {self.__altura} m")

    # Getters y setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_dni(self):
        return self.__dni
