from calculadora_indices import calcular_calorias_en_reposo
from validaciones import obtener_altura, obtener_peso, obtener_edad, obtener_valor_genero_calorias


def calculo_calorias_en_reposo():
    peso = obtener_peso()
    altura = obtener_altura()
    edad = obtener_edad()
    valor_genero = obtener_valor_genero_calorias()
    carlorias_quemadas = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print(f"Cantidad de calorias que quema en reposo son: {carlorias_quemadas:.2f}")
    return carlorias_quemadas


def main():
    calculo_calorias_en_reposo()


if __name__ == '__main__':
    main()
