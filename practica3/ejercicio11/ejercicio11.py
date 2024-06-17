# 11- Se necesita desarrolla un programa para facturar. Ingresar Artículo, precio unitario y cantidad llamar
# a una función que calcule el importe total de la venta. También desarrollar una función de determine
# si se le debe realizar un descuento o no. Si la venta es superior a $15000 debe realizar un
# descuento del 8% si es mayor a $30000 15%. Mostrar el total de la venta y el descuento.


def get_item(item, price, quantitative):
    item_detail = {'name': item, 'price': price, 'quantity': quantitative}
    return item_detail


def get_total_price(item_detail):
    return item_detail['price'] * item_detail['quantity']


def get_discount(item_detail):
    price_to_pay = get_total_price(item_detail)
    discount = 0
    if price_to_pay > 30000:
        discount = price_to_pay * 0.15
    elif price_to_pay > 15000:
        discount = price_to_pay * 0.08
    return discount


def main():
    try:
        item_name = input("Ingrese el nombre del artículo: ")
        item_price = float(input("Ingrese el precio unitario del artículo: "))
        item_quantity = int(input("Ingrese la cantidad que desea adquirir: "))

        item_detail = get_item(item_name, item_price, item_quantity)
        total_check_out = get_total_price(item_detail)

        print(f"Total: {total_check_out}")

        if total_check_out > 15000:
            discount = get_discount(item_detail)
            price_after_discount = total_check_out - discount
            print(f"Se aplicó un descuento de ${discount:.2f}.")
            print(f"Total con descuento: ${price_after_discount:.2f}")

    except ValueError:
        print("Error: Ingrese un numero valido para el precio y la cantidad")


if __name__ == "__main__":
    main()
