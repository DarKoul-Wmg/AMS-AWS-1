lista = ["Claudia", "Diego", "Silvia", "Moisés", "Shayel", "Laura", "Maribel"]


# CON MÉTODO BURBUJA.
def invertir_lista_burbuja(lista):
    # 1. El bucle externo se ejecuta n-1 veces, donde n es la longitud de la lista.
    # La razón detrás de n-1 es que después de cada pasada, el elemento más grande se
    # coloca en su posición correcta, por lo que no es necesario revisar la última
    # posición después de la primera pasada, la penúltima después de la segunda, y
    # así sucesivamente. En la última pasada, solo se comparará e intercambiará el
    # primer elemento con el segundo si es necesario.

    # 2. Bucle Interno (for j in range(0, n-i-1):):
    # El bucle interno se encarga de recorrer la lista y realizar las comparaciones
    # y swaps necesarios.
    # range(0, n-i-1) asegura que en cada pasada del bucle externo, no se considere
    # el último elemento de la lista (que ya está en su posición correcta después de
    # las pasadas anteriores). La cantidad de comparaciones necesarias disminuye en
    # cada pasada, ya que el elemento más grande ya se encuentra en su posición
    # correcta.

    n = len(lista)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


lista_invertida_burbuja = invertir_lista_burbuja(lista.copy())

print("· Lista invertida (método burbuja):")
for elemento in lista_invertida_burbuja:
    print(elemento)


# SIN MÉTODO BURBUJA.
def invertir_lista_sin_burbuja(lista):
    return lista[::-1]


lista_invertida_sin_burbuja = invertir_lista_sin_burbuja(lista.copy())
print("\n· Lista invertida (sin método burbuja):")
for elemento in lista_invertida_sin_burbuja:
    print(elemento)

print("\n-----------------------------\nNUMERADA\n-----------------------------\n")


# NUMERADA.
def imprimir_lista_numerada(lista):
    for i, elemento in enumerate(lista, 1):
        print(f"{i}. {elemento}")


# CON MÉTODO BURBUJA.
def invertir_lista_burbuja(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


lista_invertida_burbuja = invertir_lista_burbuja(lista.copy())

print("· Lista invertida (método burbuja):")
imprimir_lista_numerada(lista_invertida_burbuja)


# SIN MÉTODO BURBUJA.
def invertir_lista_sin_burbuja(lista):
    return lista[::-1]


lista_invertida_sin_burbuja = invertir_lista_sin_burbuja(lista.copy())
print("\n· Lista invertida (sin método burbuja):")
imprimir_lista_numerada(lista_invertida_sin_burbuja)
