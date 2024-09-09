# main.py

from cuenta_bancaria import CuentaBancaria, CuentaPlazoFijo, CuentaVip
from datetime import datetime, timedelta


def main():
    cuenta1 = CuentaBancaria("Juan Pérez", datetime.now(), "001", 500)
    cuenta2 = CuentaPlazoFijo("Maria Gómez", datetime.now(), "002", 1000, datetime.now() + timedelta(days=30))
    cuenta3 = CuentaVip("Carlos López", datetime.now(), "003", 200, 500)

    cuentas = [cuenta1, cuenta2, cuenta3]

    print("Información inicial de las cuentas:")
    for cuenta in cuentas:
        print(cuenta)

    cuenta1.ingresar_dinero(300)
    cuenta2.ingresar_dinero(200)
    cuenta3.ingresar_dinero(400)

    cuenta1.retirar_dinero(200)
    cuenta2.retirar_dinero(500)
    cuenta3.retirar_dinero(600)

    cuenta1.transferir_dinero(cuenta2, 300)
    cuenta3.transferir_dinero(cuenta1, 100)

    print("\nInformación final de las cuentas:")
    for cuenta in cuentas:
        print(cuenta)


if __name__ == "__main__":
    main()
