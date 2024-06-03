
def do_pasada(lista):
    resultado = []
    if len(lista)==1:
        resultado.append(lista[0])
        return resultado

    if lista[0] > lista[1]:
        lista[0], lista[1] = lista[1], lista[0]
    resultado.append(lista[0])


    resultado = resultado + do_pasada(lista[1:])
    return resultado


def do_burbuja(lista):
    resultado = []

    if len(lista)==1:
        resultado = lista
        return resultado

    lista_despues_pasada = do_pasada(lista)
    resultado.insert(0,lista_despues_pasada[-1])

    resultado = do_burbuja(lista_despues_pasada[0:-1]) + resultado
    return resultado

lista =[3,7,3,6,2,4,9]

print(do_burbuja(lista))
