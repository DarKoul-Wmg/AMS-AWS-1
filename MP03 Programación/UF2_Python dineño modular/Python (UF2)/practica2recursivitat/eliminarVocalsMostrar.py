def eliminar_vocales(frase):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙ"
    if not frase:
        return ""
    elif frase[0] in vocales:
        return eliminar_vocales(frase[1:])
    else:
        return frase[0] + eliminar_vocales(frase[1:])


frase = "Hola, mundo. ¿Qué tal?"
print("Frase sin vocales:", eliminar_vocales(frase))
