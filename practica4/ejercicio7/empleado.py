class Empleado:
    """Clase base para todos los empleados de la empresa."""

    def __init__(self):
        """Inicializa el salario base de un empleado."""
        self.sueldo_base = 1000

    def calcular_sueldo(self):
        """Método para calcular el sueldo. Será sobrescrito en las clases derivadas."""
        return self.sueldo_base


class Jefe(Empleado):
    """Clase derivada que representa a un jefe."""

    def __init__(self, antiguedad):
        """Inicializa un jefe con su antigüedad."""
        super().__init__()
        self.antiguedad = antiguedad

    def calcular_sueldo(self):
        """Calcula el sueldo de un jefe."""
        return self.sueldo_base + (100 * self.antiguedad)


class Viajante(Empleado):
    """Clase derivada que representa a un viajante."""

    def __init__(self, viajes):
        """Inicializa un viajante con el número de viajes realizados."""
        super().__init__()
        self.viajes = viajes

    def calcular_sueldo(self):
        """Calcula el sueldo de un viajante."""
        return self.sueldo_base + (300 * self.viajes)
