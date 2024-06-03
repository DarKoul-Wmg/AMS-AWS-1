# ----------------------------------------------------------------------------------------------------------------------
print("Ejercicio 1:")
def max(n1, n2):
    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
    else:
        print("Son iguales.")


max(6, 2)
max(20, 11)

# ----------------------------------------------------------------------------------------------------------------------
print("\nEjercicio2:")


def largo_cadena(llista):
    cont = 0
    for i in llista:
        cont += 1
    return cont


print(largo_cadena([1, 2, 3, 4]))


# ----------------------------------------------------------------------------------------------------------------------
print("\nEjercicio 3:")


def es_vocal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False


print(es_vocal("a"))
print(es_vocal("A"))
print(es_vocal("1"))

# ----------------------------------------------------------------------------------------------------------------------
print("\nEjercicio 4:")


def inversa(cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida


print(inversa("asca"))
print(inversa("Claudia"))
print(inversa("Diego"))
