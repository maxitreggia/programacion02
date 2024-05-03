# Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. Permitir
# almacenar distintas actividades para la misma fecha (se ingresa la hora y la actividad)
# Implementar las siguientes actividades:
#  Carga de datos en la agenda.
#  Listado completo de la agenda.
#  Consulta de una fecha.

agenda = {}
while True:
    date = input("Ingrese la fecha (en formato dd/mm/aaaa) (o escriba 'fin' para terminar): ")
    if date.lower() == "fin":
        break
    time = input(f"Ingrese la hora para la fecha {date} (en formato hh:mm): ")
    activity = input(f"Ingrese la actividad para la fecha {date} y hora {time}: ")

    if date in agenda:
        agenda[date].append((time, activity))
    else:
        agenda[date] = [(time, activity)]

print("Listado completo de la agenda:")
for date, activities in agenda.items():
    print(f"Fecha: {date}")
    for time, activity in activities:
        print(f"\tHora: {time}, Actividad: {activity}")

query_date = input("Ingrese la fecha a consultar (en formato dd/mm/aaaa): ")
if query_date in agenda:
    activities_date = agenda[query_date]
    print(f"Actividades para la fecha {query_date}:")
    for time, activity in activities_date:
        print(f"\tHora: {time}, Actividad: {activity}")
else:
    print("No hay actividades para la fecha especificada.")
