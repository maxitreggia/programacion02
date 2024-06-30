from calculadora_indices import calcular_imc
from validaciones import obtener_altura, obtener_peso


def calculo_imc():
    peso = obtener_peso()
    altura = obtener_altura()
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")
    return imc


def main():
    calculo_imc()


if __name__ == '__main__':
    main()
