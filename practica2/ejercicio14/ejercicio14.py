# Crear un diccionario en Python que defina como clave el número de documento de una
# persona y como valor un string con su nombre. Desarrollar las siguientes funciones:
# 1) Cargar por teclado los datos de 4 personas.
# 2) Listado completo del diccionario.
# 3) Consulta del nombre de una persona ingresando su número de documento

people = {}
for _ in range(4):
    document = input("Ingrese el número de documento de la persona: ")
    name = input("Ingrese el nombre de la persona: ")
    people[document] = name

print("Listado completo del diccionario:")
for document, name in people.items():
    print(f"Número de documento: {document}, Nombre: {name}")

inquire_document = input("Ingrese el número de documento de la persona a consultar: ")
if inquire_document in people:
    person_name = people[inquire_document]
    print(f"El nombre de la persona con número de documento {inquire_document} es: {person_name}")
else:
    print("El número de documento ingresado no corresponde a ninguna persona en el diccionario.")
