def obtener_peso():
    while True:
        try:
            peso = float(input("Introduzca su peso en kilogramos: "))
            if peso <= 0 or peso > 350:
                raise ValueError("El peso debe ser un número positivo y razonable.")
            return peso
        except ValueError as e:
            print(f"Entrada no válida: {e}. Por favor, intente nuevamente.")


def obtener_altura():
    while True:
        try:
            altura = float(input("Introduzca su altura en metros: "))
            if altura <= 0 or altura > 3:
                raise ValueError("La altura debe ser un número positivo y razonable.")
            return altura
        except ValueError as e:
            print(f"Entrada no válida: {e}. Por favor, intente nuevamente.")


def obtener_edad():
    while True:
        try:
            edad = int(input("Introduzca su edad: "))
            if edad <= 0 or edad > 118:
                raise ValueError("La edad debe ser un número positivo y razonable.")
            return edad
        except ValueError as e:
            print(f"Entrada no válida: {e}. Por favor, intente nuevamente.")


def obtener_valor_genero_porcentaje_grasa():
    while True:
        try:
            genero = int(input("Por favor, seleccione su género: \n1. Masculino \n2. Femenino \nIntroduzca 1 o 2: "))
            if genero not in [1, 2]:
                raise ValueError("Debe introducir 1 0 2")

            valor_genero = 10.8 if genero == 1 else 0
            return valor_genero
        except ValueError as e:
            print(f"Entrada no válida: {e}. Por favor, intente nuevamente.")


def obtener_valor_genero_calorias():
    while True:
        try:
            genero = int(input("Por favor, seleccione su género: \n1. Masculino \n2. Femenino \nIntroduzca 1 o 2: "))
            if genero not in [1, 2]:
                raise ValueError("Debe introducir 1 0 2")

            valor_genero = 5 if genero == 1 else -161
            return valor_genero
        except ValueError as e:
            print(f"Entrada no válida: {e}. Por favor, intente nuevamente.")


def obtener_valor_actividad():
    while True:
        try:
            valor_actividad = 0
            actividad = int(input("Por favor, seleccione cuanta actividad realiza por semana:\n1. Poco o ningún "
                                  "ejercicio\n2. Ejercicio ligero (1 a 3 días a la semana)\n3. Ejercicio moderado (3 "
                                  "a 5 días a la semana)\n4. Deportista (6 -7 días a la semana)\n5. Atleta ("
                                  "entrenamientos mañana y tarde)\n Ingrese un opcion:"))
            match actividad:
                case 1:
                    valor_actividad = 1.2
                case 2:
                    valor_actividad = 1.375
                case 3:
                    valor_actividad = 1.55
                case 4:
                    valor_actividad = 1.725
                case 5:
                    valor_actividad = 1.9
            return valor_actividad
        except ValueError as e:
            print(f"Entrada no válida: {e}. Por favor, intente nuevamente.")
