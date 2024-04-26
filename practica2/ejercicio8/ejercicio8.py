# En un curso de n alumnos se registraron las notas de sus exámenes y se deben procesar
# de acuerdo a lo siguiente:
# a) Ingresar nombre y nota de cada alumno
# b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la
# condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está
# entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
# c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

number_of_students = int(input("Ingrese la cantidad de estudiantes: "))
list_students = []
note_of_students = []
higher_than_eight = 0

for i in range(number_of_students):
    list_students.append(input(f"Ingrese el nombre del estudiante{i + 1}/{number_of_students}: ").upper())
    note_of_students.append(int((input(f"Ingrese la nota del estudiante{i + 1}/{number_of_students}: "))))

for i in range(number_of_students):
    if note_of_students[i] >= 8:
        list_students[i] += " Muy bueno"
        higher_than_eight += 1
    elif 7 <= note_of_students[i] >= 4:
        list_students[i] += " Bueno"
    else:
        list_students[i] += " Insuficiente"

print(f"Lista de estudiantes y sus estados {list_students}")
print(f"Cantidad de alumnos con \"Muy Bueno\": {higher_than_eight}")
