# 9- Desarrollar un programa (función) que calcule en interes que nos dará un plazo Fijo para lo cual se
# deberá ingresar el Capital, la tasa y la cantidad de días del mismo. Utilizar la Fórmula de interés
# simple - (C*R*T)/ 100*UT . Mostrar el interés a percibir.


def valid_positive_number(number):
    return number >= 0


def valid_int_number(number):
    try:
        return int(number)
    except ValueError:
        print("Error: ingrese un numero entero")
        return None


def valid_float_number(number):
    try:
        return float(number)
    except ValueError:
        print("Error: ingrese un numero entero")
        return None


def get_rate_per_day(rate):
    return rate/365


def get_fixed_term_deposit(rate, capital, days):
    rate_per_day = get_rate_per_day(rate)
    interest_earned = (capital * rate_per_day * days)/100
    return interest_earned


def get_input_from_user():
    while True:
        capital = float(input("Ingrese el capital:"))
        capital = valid_float_number(capital)
        if capital is not None and valid_positive_number(capital):
            break
        else:
            print("Error: ingrese un numero valido")

    while True:
        days = int(input("Ingrese la cantidad de dias del plazo fijo:"))
        days = valid_int_number(days)
        if days is not None and valid_positive_number(days):
            break
        else:
            print("Error: ingrese un numero valido")

    while True:
        rate = float(input("Ingrese el interes anual:"))
        rate = valid_float_number(rate)
        if rate is not None and valid_positive_number(rate):
            break
        else:
            print("Error: ingrese un numero valido")

    return capital, days, rate


def main():
    capital, days, rate = get_input_from_user()
    interest = get_fixed_term_deposit(capital, days, rate)
    print(f"El interes generado es: {interest:.2f}")


if __name__ == "__main__":
    main()
