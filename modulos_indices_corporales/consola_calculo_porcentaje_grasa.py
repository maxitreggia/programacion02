from calculadora_indices import calcular_porcentaje_grasa
from validaciones import obtener_altura, obtener_peso, obtener_edad, obtener_valor_genero_porcentaje_grasa


def calculo_porcentaje_grasa():
    peso = obtener_peso()
    altura = obtener_altura()
    edad = obtener_edad()
    valor_genero = obtener_valor_genero_porcentaje_grasa()
    porcentaje_grasa = calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print(f"Su porcentaje de grasa es: {porcentaje_grasa:.2f}")
    return porcentaje_grasa


def main():
    calculo_porcentaje_grasa()


if __name__ == '__main__':
    main()
