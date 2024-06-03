lista = [1,2,3,4]
numero = 10
def funcion(lista_numeros):
    lista_numeros[2] = 1000 #LISTA SE MODIFICA, VARIABLE NORMAL NO

def funcionB(num):
    num = 1000

funcionB(numero)
funcion(lista)
funcion(lista[1:]) #SI ALTERAMOS LA LISTA, ESTA NO SE MODIFICA
print(lista)