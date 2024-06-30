from calculadora_indices import consumo_recomendado_para_adelgazar
from validaciones import obtener_altura, obtener_peso, obtener_edad, obtener_valor_genero_calorias


def calculo_consumo_recomendado_para_adelgazar():
    peso = obtener_peso()
    altura = obtener_altura()
    edad = obtener_edad()
    valor_genero = obtener_valor_genero_calorias()
    carlorias_adelgazar = consumo_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(f"{carlorias_adelgazar}")
    return carlorias_adelgazar


def main():
    calculo_consumo_recomendado_para_adelgazar()


if __name__ == '__main__':
    main()
