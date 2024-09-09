from empleado import Empleado, Jefe, Viajante
import random


def main():
    empleados = []

    for _ in range(2):
        antiguedad = random.randint(0, 10)
        empleados.append(Jefe(antiguedad))

    for _ in range(5):
        viajes = random.randint(0, 10)
        empleados.append(Viajante(viajes))

    for _ in range(15):
        empleados.append(Empleado())

    print("Salarios de los empleados de la empresa:")
    for i, empleado in enumerate(empleados, start=1):
        print(f"Empleado {i}: ${empleado.calcular_sueldo():.2f}")


if __name__ == "__main__":
    main()
