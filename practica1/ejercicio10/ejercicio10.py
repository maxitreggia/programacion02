preguntas = int(input("Ingrese la cantidad de preguntas: "))
preguntas_acertadas = int(input("Ingrese la cantidad de preguntas acertadas: "))

resultado = (preguntas_acertadas / preguntas) * 100

match resultado:
    case porcentaje if porcentaje >= 90:
        print("Nivel máximo")
    case porcentaje if porcentaje >= 75:
        print("Nivel medio")
    case porcentaje if porcentaje >= 50:
        print("Nivel regular")
    case porcentaje:
        print("Fuera de nivel")
