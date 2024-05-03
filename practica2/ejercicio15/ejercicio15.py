# Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su
# oficina cortando todas las palabras de más de cinco letras a sólo cinco letras (e indicando que
# una palabra fue cortada con el agregado de una arroba).

original_telegram = ("El oficial de correos decide optimizar el trabajo de su oficina cortando todas las palabras de "
                     "más de cinco letras a sólo cinco letras (e indicando que una palabra fue cortada con el "
                     "agregado de una arroba).")

words = original_telegram.split()
for i in range(len(words)):
    if len(words[i]) > 5:
        words[i] = words[i][:5] + '@'
processed_telegram = ' '.join(words)

print("Telegrama original:")
print(original_telegram)
print("\nTelegrama procesado:")
print(processed_telegram)
