# Almacenar en un diccionario 5 empleados y sus últimos 3 sueldos (estos tres valores en
# una tupla).
# El programa debe tener las siguientes funciones:
#  Carga de los empleados y sus sueldos
#  Carga el nombre de un empleado, buscar sus sueldos y mostrarlos.

employees = {}
for _ in range(5):
    name = input("Ingrese el nombre del empleado: ")
    salaries = tuple(float(input(f"Ingrese el sueldo {i+1} del empleado {name}: ")) for i in range(3))
    employees[name] = salaries

employee_name = input("Ingrese el nombre del empleado para buscar sus sueldos: ")
if employee_name in employees:
    employee_salaries = employees[employee_name]
    print(f"Los sueldos del empleado {employee_name} son: {employee_salaries}")
else:
    print("El empleado no fue encontrado.")
