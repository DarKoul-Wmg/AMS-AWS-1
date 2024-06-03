#dada una frase devolver la frase al revés
def frase_invertida(frase):
    resultado = ""
    if len(frase) == 0:
        return resultado

    else:
        resultado += frase[-1]
        return resultado + frase_invertida(frase[:-1])



frase = "abcdefg"
print(frase_invertida(frase))

#CLASE
def frase_al_reves(frase):
    resultado = ""
    if len(frase) == 0:
        return resultado
    else:
        resultado = frase[-1] + frase_al_reves(frase[0:-1])
        return resultado
print(frase_al_reves("cadena"))