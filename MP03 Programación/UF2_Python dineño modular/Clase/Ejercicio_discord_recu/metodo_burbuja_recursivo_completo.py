# Si modificamos la lista dentro de la funcion, se mantienen los cambios, pero si modificamos
# parte de la lista ( lista[0:-1] ) , estos cambios ya no afectan a la lista original
# por tanto, lo que haremos será devolver la lista después de cada pasada
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

lista = [8,3,7,9,2]
print(do_pasada(lista))
