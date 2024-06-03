#dada una lista de números, devolver una lista con los números pares (repetidos si salen más de una vez)

def listaPar(lista):
    resultado = []
    if len(lista) == 0:
        return resultado

    if lista[0] %2 == 0:
        resultado.append(lista[0])
    
    return resultado + listaPar(lista[1:])






lista = [1,2,2,3,6,8,8,9]
print(listaPar(lista))
