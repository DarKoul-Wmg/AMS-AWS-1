def sumaLista(lista):
    if len(lista) == 0:
        return 0

    return lista[0] + sumaLista(lista[1:])


lista = [1,2,3,4]
resultado = sumaLista(lista)
print(resultado)

#CLASE
def sumaLista2(lista):
    resultado = 0
    if len(lista) == 0:
        return resultado
    else:
        resultado = lista[0] + sumaLista2(lista[1:])
        return resultado

print(sumaLista2(lista))
