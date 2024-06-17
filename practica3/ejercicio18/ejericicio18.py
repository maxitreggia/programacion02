# 18- Realizar una función que permita calcular el total de ventas diarias. La cantidad de ventas varia
# diariamente. La función debe retornar ese total.


def get_total_revenue(sales):
    return sum(sales)


def main():
    sales = []
    while True:
        sale_input = input("Ingrese el valor de la venta (o presione Enter para salir): ")
        if sale_input == "":
            break
        try:
            sale = float(sale_input)
            if sale < 0:
                print("El valor de la venta debe ser positivo")
            else:
                sales.append(sale)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    total = get_total_revenue(sales)
    print(f"El total de las ventas es: {total}")


if __name__ == '__main__':
    main()
