lista = [1,2,3,4]

def sum(lista):
    suma = 0
    for element in lista:
        suma += element

    return suma


def multip(lista):
    multi = 0
    for element in lista:
        if element is lista[0]:
            multi += element
        else:
            multi *= element

    return multi

print("Suma "+str(sum(lista)))
print("Multiplicació "+ str(multip(lista)))
