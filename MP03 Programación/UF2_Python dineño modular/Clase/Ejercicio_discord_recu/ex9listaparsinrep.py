def numeros_pares_no_rep(lista):
    resultado = []

    if len(lista) ==0:
        return lista
    else:
        resultado = numeros_pares_no_rep(lista[1:])
        if lista[0] %2 == 0 and lista[0] not in resultado:
            resultado.append(lista[0])
        return resultado

lista = [1,2,2,3,6,8,8,9]
print(numeros_pares_no_rep(lista))
