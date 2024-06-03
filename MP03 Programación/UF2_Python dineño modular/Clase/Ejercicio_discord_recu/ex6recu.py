#dada una frase devolver la frase con vocales a mayúsculas y consonantes en minúsculas

#CLASE
def funcion_VoMa_CoMi(cadena):
    vocales = "aeiou"
    resultado = ""
    if len(cadena) == 0:
        return resultado

    elif cadena[0].lower() in vocales:
        resultado = cadena[0].upper() + funcion_VoMa_CoMi(cadena[1:])

    else:
        resultado = cadena[0].lower() + funcion_VoMa_CoMi(cadena[1:])

    return resultado

print(funcion_VoMa_CoMi(cadena))