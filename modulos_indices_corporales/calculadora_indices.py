def calcular_imc(peso: float, altura: float) -> float:
    imc = peso / altura ** 2
    return round(imc, 2)


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    imc = calcular_imc(peso, altura)
    return 1.2 * imc + 0.23 * edad - 5.4 - valor_genero


def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    altura_cm = altura * 100
    return (10 * peso) + (6.25 * altura_cm) - (5 * edad) + valor_genero


def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: float,
                                   valor_actividad: float) -> float:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return tmb * valor_actividad


def consumo_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float) -> str:
    calorias_reposo = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    calorias_min = calorias_reposo * 0.80
    calorias_max = calorias_reposo * 0.85
    return f"Para adelgazar, se recomienda consumir entre {calorias_min:.2f} y {calorias_max:.2f} calorías al día."
