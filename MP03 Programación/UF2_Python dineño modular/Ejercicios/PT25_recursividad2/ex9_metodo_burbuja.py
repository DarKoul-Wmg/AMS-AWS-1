
def do_pasada(lista):
    resultado = []
    # si solo tenemos un número en la lista, añadimos el numero al resultado y lo devolvemos
    if len(lista)==1:
        resultado.append(lista[0])
        return resultado
    # si tenemos mas elementos, comparamos el primer elemento de la lista con el segundo, añadimos el primer
    # elemento al resultado, ya que éste no se modificará, y realizamos el mismo proceso con el resto de
    # la lista ( es decir , la lista sin el primer elemento).
    if lista[0] > lista[1]:
        lista[0], lista[1] = lista[1], lista[0]
    resultado.append(lista[0])
    # a resultado le vamos añadiendo los resultados de las llamadas con las listas parciales, es decir, las
    # llamadas con la lista menos primer elemento
    resultado = resultado + do_pasada(lista[1:])
    return resultado

#Este algoritmo realiza len(lista)-1 llamadas la función recursiva que realiza una pasada. Y lo hace
# también de forma recursiva. nos devolverá la lista ordenada.
def do_burbuja(lista):
    resultado = []
    #si sólo hay un elemento, devolvemos una lista con este elemento.
    if len(lista)==1:
        resultado = lista
        return resultado
    # si tenemos más elementos, realizamos una pasada llamando a la funcion recursiva do_pasada
    # guardamos el resultado en lista_despues_pasada. Este resultado tendrá ordenado el último elemento
    #por tanto, añadimos este elemento al resultado.
    lista_despues_pasada = do_pasada(lista)
    resultado.insert(0,lista_despues_pasada[-1])
    # como los elementos ordenados siempre quedan al final, concatenamos el resultado de realizar una llamada
    # recursiva a new_pasada con todos los elementos de la lista excepto el último
    resultado = do_burbuja(lista_despues_pasada[0:-1]) + resultado
    return resultado

lista =[3,7,3,6,2,4,9]

print(do_burbuja(lista))
