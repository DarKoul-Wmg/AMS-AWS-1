def multi_array(lista):
    resultado = 1
    if len(lista) == 1:
        resultado = lista[0]
        return resultado
    else:
        resultado = resultado * lista[0]
        return resultado * multi_array(lista[1:])

lista = [1,2,3,4]
print(multi_array(lista))
