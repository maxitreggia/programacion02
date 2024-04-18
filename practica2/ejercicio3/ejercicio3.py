# Crea un programa que pida una frase al usuario y la transforme en una lista donde cada
# elemento sea las palabras que forman la frase.

phrase = input("Ingrese una frasw: ")

phrase_to_list = phrase.split(" ")

print(f"La frase ingresada es: {phrase}")
print(f"La frase convertida a lista es: {phrase_to_list}")