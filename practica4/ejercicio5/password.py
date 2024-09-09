import random
import string


class Password:
    def __init__(self, longitud=8):
        """Constructor de la clase Password. Genera una contraseña según la longitud especificada."""
        self.__longitud = longitud
        if self.__longitud == 0:
            self.__contraseña = "password"
        else:
            self.__contraseña = self.generarPassword()

    def esFuerte(self):
        """Devuelve True si la contraseña es fuerte, de lo contrario False."""
        mayusculas = sum(1 for c in self.__contraseña if c.isupper())
        minusculas = sum(1 for c in self.__contraseña if c.islower())
        numeros = sum(1 for c in self.__contraseña if c.isdigit())

        return mayusculas > 2 and minusculas > 1 and numeros > 5

    def generarPassword(self):
        """Genera una contraseña aleatoria de la longitud especificada."""
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(self.__longitud))

    def get_contraseña(self):
        """Devuelve la contraseña."""
        return self.__contraseña

    def get_longitud(self):
        """Devuelve la longitud de la contraseña."""
        return self.__longitud

    def set_longitud(self, longitud):
        """Establece una nueva longitud para la contraseña y la regenera."""
        self.__longitud = longitud
        self.__contraseña = self.generarPassword()
