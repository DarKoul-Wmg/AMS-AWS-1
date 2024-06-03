""" Exercici 3:
Una paraula és alfabètica si totes les seves lletres estan ordenades alfabèticament. Per exemple, amor, és una paraula
alfabètica. Dissenya un programa que llegeixi una paraula i ens digui si es alfabètica o no. """


def es_alfabetica(palabra):
    # Convertir la palabra en una lista de caracteres.
    caracteres = list(palabra)

    # Ordenar la lista de caracteres alfabéticamente.
    caracteres_ordenados = sorted(caracteres)

    # Verificar si la palabra original y la palabra ordenada son iguales.
    return caracteres == caracteres_ordenados


# Leer la palabra desde la entrada estándar.
palabra = input("Introduce una palabra.\n> ")

# Determinar si la palabra es alfabética o no.
if es_alfabetica(palabra):
    print("La palabra es alfabética.")
else:
    print("La palabra no es alfabética.")


# Sin sorted:
def es_alfabetica(palabra):
    # Convertir la palabra en una lista de caracteres.
    caracteres = list(palabra)

    # Implementar el algoritmo de ordenación burbuja.
    n = len(caracteres)
    for i in range(n):
        for j in range(0, n-i-1):
            if caracteres[j] > caracteres[j+1]:
                # Intercambiar los caracteres si están en el orden incorrecto.
                caracteres[j], caracteres[j+1] = caracteres[j+1], caracteres[j]

    # Verificar si la palabra original y la palabra ordenada son iguales.
    return caracteres == list(palabra)


# Leer la palabra desde la entrada estándar.
palabra = input("Introduce una palabra.\n> ")

# Determinar si la palabra es alfabética o no.
if es_alfabetica(palabra):
    print("La palabra es alfabética.")
else:
    print("La palabra no es alfabética.")
