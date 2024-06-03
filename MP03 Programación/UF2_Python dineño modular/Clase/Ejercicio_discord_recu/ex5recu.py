#dada una frase devolver el número de vocales
def vocales(frase):
    cont = ""
    vocal = "aeiou"
    if len(frase) == 0:
        return len(cont)

    else:
        if frase[0] in vocal:
            cont += frase[0]
            return cont + vocales(frase[1:])
        else:
            cont += frase[0]
            return vocales(frase[1:]) + cont


#frase = "eeddaaas"
print(vocales("abcdefg"))

#CLASE

def num_vocales(cadena):
    vocales = "aeiou"
    resultado = 0
    if len(cadena) == 0:
        return resultado

    elif cadena[0].lower() in vocales:
        resultado = 1 + num_vocales(cadena[1:])

    else:
        resultado = num_vocales(cadena[1:])
    return resultado
print(num_vocales(cadena))