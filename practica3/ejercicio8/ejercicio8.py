# 8- Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que
# las palabras están separadas por uno o más espacios. También podría haber espacios al principio
# o al final del string pasado por parámetro.

import re

text_to_separate = (str(input("Ingrese un texto: ")))


def clean_spaces(text):
    text = text.strip()
    clean_text = re.sub(r"\s+", " ", text)
    return clean_text


def split_string(text_to_split):
    text_to_split = clean_spaces(text_to_split)
    return text_to_split.split()


def len_last_word(text):
    text = split_string(text)
    return len(text[-1])


print(f"La ultima palabra tiene {len_last_word(text_to_separate)} caracteres")
