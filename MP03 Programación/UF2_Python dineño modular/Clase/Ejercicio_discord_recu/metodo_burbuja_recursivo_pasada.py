#algoritmo de la burbuja realiza n-1 pasadas, y en cada pasada, se ordenan los elementos de 0 a (n-1-pasada).
#Podemos realizar un algoritmo totalmente recursivo que reciba como único parámetro la lista que queremos ordenar y realice una pasada?
#Este algoritmo retornará (importante lo de "retornará") la lista después de realizar una pasada
#si llamamos a este algoritmo pasándole como parámetro [9,8,7,6] nos devolverá la lista [8,7,6,9]

def ordenBurbuja(lista):
    resultado = []
    if len(lista) == 1:
        resultado.append(lista[0])
        return resultado

    elif lista[0] > lista[1]:
        aux = lista[0]
        lista[0] = lista[1]
        lista[1] = aux

    resultado.append(lista[0])

    return resultado + ordenBurbuja(lista[1:])

lista = [8,9,7,6]
print(ordenBurbuja(lista))
