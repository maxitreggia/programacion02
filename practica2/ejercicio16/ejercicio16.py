# Se desea saber la temperatura media trimestral de n países. Para ello se tiene como dato
# las temperaturas medias mensuales de dichos países.
# Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias
# mensuales.
# Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en
# memoria.
# a - Cargar por teclado los nombres de los países y las temperaturas medias mensuales.
#
# b - Imprimir los nombres de las países y las temperaturas medias mensuales de las mismas.
# c - Calcular la temperatura media trimestral de cada país.
# c - Imprimir los nombres de los países y las temperaturas medias trimestrales.
# b - Imprimir el nombre del país con la temperatura media trimestral mayor.

temperatures = {}
num_countries = int(input("Ingrese el número de países: "))
for _ in range(num_countries):
    country = input("Ingrese el nombre del país: ")
    monthly_temperatures = []
    for month in range(1, 4):
        temperature = float(input(f"Ingrese la temperatura media del mes {month} para {country}: "))
        monthly_temperatures.append(temperature)
    temperatures[country] = monthly_temperatures

print("Temperaturas medias mensuales:")
for country, monthly_temperatures in temperatures.items():
    print(f"{country}: {monthly_temperatures}")

quarterly_temperatures = {}
for country, monthly_temperatures in temperatures.items():
    quarterly_temperatures[country] = sum(monthly_temperatures) / len(monthly_temperatures)

print("Temperaturas medias trimestrales:")
for country, quarterly_temperature in quarterly_temperatures.items():
    print(f"{country}: {quarterly_temperature}")

country_max_temp = max(quarterly_temperatures, key=quarterly_temperatures.get)
max_temp = quarterly_temperatures[country_max_temp]
print(f"El país con la temperatura media trimestral más alta es {country_max_temp} con {max_temp} grados.")
