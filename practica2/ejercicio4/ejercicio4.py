# En una lista se almacenan los componentes de una dirección IP juntarlos en una variable
# y mostrarlos.

ip_list = [192, 181, 6, 1]

ip_to_string = ".".join(map(str, ip_list))

print(f"Su ip es: {ip_to_string}")
