#dado un string devolver una lista con todas las vocales (repetidas si salen más de una vez)
#que aparecen en el string

def lista_vocales(cadena):
    lista = []
    vocales = "aeiou"

    if len(cadena) == 0:
        return lista

    elif cadena[0] in vocales:
        lista.append(cadena[0])
        return lista + lista_vocales(cadena[1:])

    return lista + lista_vocales(cadena[1:])

cadena = "antonio"
print(lista_vocales(cadena))
