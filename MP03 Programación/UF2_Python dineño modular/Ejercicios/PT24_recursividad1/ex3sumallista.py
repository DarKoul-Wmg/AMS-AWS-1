def suma_lista(lista):
    resultado = 0
    if len(lista) == 0:
        return resultado
    else:
        resultado += lista[0]
        return resultado + suma_lista(lista[1:])




lista1 = [1,2,3,4]
#lista2 = ["a","w","m"]
print(suma_lista(lista1))
