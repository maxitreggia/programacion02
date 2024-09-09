class DateError(Exception):
    """Excepción personalizada para errores de fecha."""
    def __init__(self, message):
        super().__init__(message)


class Fecha:
    """Clase para representar una fecha con validación."""

    # Días máximos por mes (no considera años bisiestos)
    DIAS_POR_MES = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    def __init__(self, dia, mes, año):
        """Constructor que valida la fecha al crear una instancia."""
        self.setDia(dia)
        self.setMes(mes)
        self.setAño(año)

    def getDia(self):
        """Devuelve el día de la fecha."""
        return self.dia

    def getMes(self):
        """Devuelve el mes de la fecha."""
        return self.mes

    def getAño(self):
        """Devuelve el año de la fecha."""
        return self.año

    def setDia(self, dia):
        """Modifica el día de la fecha, validando que sea correcto."""
        if not 1 <= dia <= 31:
            raise DateError(f"El día {dia} no es válido.")
        if hasattr(self, 'mes') and not self.__dia_valido(dia, self.mes):
            raise DateError(f"El día {dia} no es válido para el mes {self.mes}.")
        self.dia = dia

    def setMes(self, mes):
        """Modifica el mes de la fecha, validando que sea correcto."""
        if not 1 <= mes <= 12:
            raise DateError(f"El mes {mes} no es válido.")
        self.mes = mes
        if hasattr(self, 'dia') and not self.__dia_valido(self.dia, mes):
            raise DateError(f"El día {self.dia} no es válido para el mes {mes}.")

    def setAño(self, año):
        """Modifica el año de la fecha."""
        if año < 1:
            raise DateError(f"El año {año} no es válido.")
        self.año = año

    def __dia_valido(self, dia, mes):
        """Valida que el día sea correcto para el mes dado."""
        return 1 <= dia <= self.DIAS_POR_MES[mes]

    def __str__(self):
        """Devuelve la fecha como una cadena en formato DD/MM/AAAA."""
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"
