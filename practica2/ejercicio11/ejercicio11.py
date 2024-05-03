# Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. La clave
# es la palabra en inglés y el valor es la palabra en castellano.
#  Cargar el diccionario.
#  Listado completo del diccionario.
#  Ingresar por teclado una palabra en inglés y si existe en el diccionario mostrar su
# traducción.

dictionary = {}
while True:
    english_word = input("Ingrese una palabra en inglés (o escriba 'fin' para terminar): ")
    if english_word.lower() == "fin":
        break
    spanish_word = input(f"Ingrese la traducción de '{english_word}' en castellano: ")
    dictionary[english_word] = spanish_word

# Mostrar el diccionario completo
print("Diccionario completo:")
for english_word, spanish_word in dictionary.items():
    print(f"{english_word}: {spanish_word}")

# Ingresar una palabra en inglés para traducir
english_word = input("Ingrese una palabra en inglés para traducir: ")
if english_word in dictionary:
    translation = dictionary[english_word]
    print(f"La traducción de '{english_word}' es: {translation}")
else:
    print("La palabra no fue encontrada en el diccionario.")
