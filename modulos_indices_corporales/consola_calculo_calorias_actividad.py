from calculadora_indices import calcular_calorias_en_actividad
from validaciones import (obtener_altura, obtener_peso, obtener_edad, obtener_valor_genero_calorias,
                          obtener_valor_actividad)


def calculo_calorias_en_actividad():
    peso = obtener_peso()
    altura = obtener_altura()
    edad = obtener_edad()
    valor_genero = obtener_valor_genero_calorias()
    valor_actidad = obtener_valor_actividad()
    carlorias_quemadas = calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actidad)
    print(f"Cantidad de calorias que quema en actividad son: {carlorias_quemadas:.2f}")
    return carlorias_quemadas


def main():
    calculo_calorias_en_actividad()


if __name__ == '__main__':
    main()
