#dada una frase y una letra, devolver la frase desde el principio hasta la letra
def letra_to_principio(cadena,letra):
    if len(cadena) == 0:
        return cadena

    elif cadena[-1] == letra:
        return cadena

    else:
        return letra_to_principio(cadena[0:-1],letra)

cadena = "abcdefgh"
letra = "e"
print(letra_to_principio(cadena,letra))
