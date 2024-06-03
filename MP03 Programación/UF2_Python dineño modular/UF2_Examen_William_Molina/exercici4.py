import random

def exercici4(lista1,lista2):
    resultado = []
    if len(lista1) == 0 and len(lista2) == 0:
        return resultado

    elif len(lista1) == 0 and len(lista2) != 0:
        resultado = exercici4(lista1,lista2[1:])

    elif len(lista1) != 0 and len(lista2) == 0:
        resultado = exercici4(lista1[1:],lista2)
    else:
        resultado = exercici4(lista1[1:],lista2[1:])

    if len(lista1) > 0 and lista1[0] in lista2 and not lista1[0] in resultado:
        resultado.append(lista1[0])

    if len(lista2) > 0 and lista2[0] in lista1 and not lista2[0] in resultado:
        resultado.append(lista2[0])

    return resultado




len1 = random.randint(0,10)
len2 = random.randint(0,10)
lista1 = []
lista2 = []

for i in range(len1):
    lista1.append(random.randint(0,15))

for j in range(len2):
    lista2.append(random.randint(0,15))
print(lista1)
print(lista2)

print(exercici4(lista1,lista2))
