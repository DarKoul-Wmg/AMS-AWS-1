import random

#Funcion devuelve lista de numeros aleatorios
#A la funcion le pasamos el numero de elementos en la lista y el rango maximo(0,num)

def lista_aleatoria(longitud,num):
    lista = []
    if longitud == 0:
        return lista

    elif longitud > 0:
        lista.append(random.randrange(num))
        return lista + lista_aleatoria(longitud-1,num)

longitud = 5
num = 100

print(lista_aleatoria(longitud,num))

