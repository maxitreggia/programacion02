from datetime import datetime


class CuentaBancaria:
    """Clase base para las cuentas bancarias."""

    def __init__(self, nombre_titular, fecha_apertura, numero_cuenta, saldo=0.0):
        self.nombre_titular = nombre_titular
        self.fecha_apertura = fecha_apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def retirar_dinero(self, cantidad):
        """Retira dinero de la cuenta si hay saldo suficiente."""
        if cantidad > self.saldo:
            print(f"Operación fallida: saldo insuficiente en la cuenta {self.numero_cuenta}.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso de ${cantidad:.2f} en la cuenta {self.numero_cuenta}.")

    def ingresar_dinero(self, cantidad):
        """Ingresa dinero en la cuenta."""
        self.saldo += cantidad
        print(f"Ingreso exitoso de ${cantidad:.2f} en la cuenta {self.numero_cuenta}.")

    def transferir_dinero(self, cuenta_destino, cantidad):
        """Transfiere dinero a otra cuenta si hay saldo suficiente."""
        if cantidad > self.saldo:
            print(f"Transferencia fallida: saldo insuficiente en la cuenta {self.numero_cuenta}.")
        else:
            self.retirar_dinero(cantidad)
            cuenta_destino.ingresar_dinero(cantidad)
            print(
                f"Transferencia de ${cantidad:.2f} de la cuenta {self.numero_cuenta} a la cuenta {cuenta_destino.numero_cuenta} exitosa.")

    def __str__(self):
        return f"Cuenta {self.numero_cuenta} de {self.nombre_titular} con saldo ${self.saldo:.2f}"


class CuentaPlazoFijo(CuentaBancaria):
    """Clase para cuentas a plazo fijo."""

    def __init__(self, nombre_titular, fecha_apertura, numero_cuenta, saldo, fecha_vencimiento):
        super().__init__(nombre_titular, fecha_apertura, numero_cuenta, saldo)
        self.fecha_vencimiento = fecha_vencimiento

    def retirar_dinero(self, cantidad):
        """Retira dinero aplicando una penalización si es antes de la fecha de vencimiento."""
        if datetime.now() < self.fecha_vencimiento:
            penalizacion = cantidad * 0.05
            total_retiro = cantidad + penalizacion
            if total_retiro > self.saldo:
                print(f"Operación fallida: saldo insuficiente en la cuenta {self.numero_cuenta}.")
            else:
                self.saldo -= total_retiro
                print(
                    f"Retiro anticipado con penalización de ${penalizacion:.2f}. Total retirado: ${total_retiro:.2f} de la cuenta {self.numero_cuenta}.")
        else:
            super().retirar_dinero(cantidad)


class CuentaVip(CuentaBancaria):
    """Clase para cuentas VIP."""

    def __init__(self, nombre_titular, fecha_apertura, numero_cuenta, saldo, saldo_negativo_maximo):
        super().__init__(nombre_titular, fecha_apertura, numero_cuenta, saldo)
        self.saldo_negativo_maximo = saldo_negativo_maximo

    def retirar_dinero(self, cantidad):
        """Permite retirar dinero incluso con saldo negativo, hasta el límite permitido."""
        if self.saldo - cantidad < -self.saldo_negativo_maximo:
            print(
                f"Operación fallida: no se puede exceder el saldo negativo máximo de ${self.saldo_negativo_maximo:.2f}.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso de ${cantidad:.2f} en la cuenta VIP {self.numero_cuenta}.")
