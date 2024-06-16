# 7- Se necesita desarrollar Programa(función)que presupueste cuánto saldrá el alambrado de un
# campo. Para ello ingresar las medidas del terrero y el precio del metro de alambre. Crear un módulo
# para calcular la cantidad de metros necesarios y calcular el costo del alambrado y mostrar el costo.

def calculate_quantitative(land_measurements):
    return sum(land_measurements)


def calculate_cost(land_measurements, cost_per_meter):
    total_land = calculate_quantitative(land_measurements)
    total_cost = total_land * cost_per_meter
    return total_cost
