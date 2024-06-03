lista1 = ["azul","verde","rojo","blanco"]
lista2 = ["negro","azul","rojo","violeta"]

palabras_iguales = []
palabras_lista1 = []
palabras_lista2 = []

for i in range(len(lista1)):
    if lista1[i] in lista2:
        palabras_iguales.append(lista1[i])
    elif not lista1[i] in lista2:
        palabras_lista1.append(lista1[i])
for i in range(len(lista2)):

    if not lista2[i] in lista1:
        palabras_lista2.append(lista2[i])

print(palabras_iguales)
print(palabras_lista1)
print(palabras_lista2)
