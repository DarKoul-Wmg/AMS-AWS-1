#dada una frase devolver vocales al principio y consonantes al final (sin importar el orden)
def vocales_consonantes(frase):
    orden = ""
    vocales = "aeiou"
    if len(frase) == 0:
        return orden

    else:
        if frase[0] in vocales:
            orden += frase[0]
            return orden + vocales_consonantes(frase[1:])
        else:
            orden += frase[0]
            return vocales_consonantes(frase[1:]) + orden



#frase = "eeddaaas"
print(vocales_consonantes("abcdefg"))

#CLASE
def vocales_y_consonantes(cadena):
    vocales = "aeiou"
    resultado = ""
    if len(cadena) == 0:
        return resultado
    elif cadena[0].lower() in vocales:
        resultado = cadena[0] + vocales_y_consonantes(cadena[1:])
    else:
        resultado = vocales_y_consonantes(cadena[1:]) + cadena[0]

    return resultado
cadena = "abcdefghi"
print(vocales_y_consonantes(cadena))