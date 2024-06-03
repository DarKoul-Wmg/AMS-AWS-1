# 1
lista_reales = []

def secuencia_reales():
    while True:
        num = float(input("Introduce un numero real mayor o igual a 0"
                          "\n-)Para acabar de introducir pon un numero negativo:\n"))
        if num >= 0:
            lista_reales.append(num)
        else:
            break
    #print(lista_reales)
    return lista_reales

# 2
def suma_reales(lista_reales):
    suma = 0
    for valor in lista_reales:
        suma += valor

    return round(suma,2)
    #print(suma)

# 3
def max_reales(lista_reales):
    maximo = lista_reales[0]

    for valor in lista_reales:
        if valor > maximo:
            maximo = valor

    #print(maximo)
    return maximo

# 4
def min_reales(lista_reales):
    minimo = lista_reales[0]

    for valor in lista_reales:
        if valor < minimo:
            minimo = valor

    #print(minimo)
    return minimo

# 5
def recorrido_reales(lista_reales):
    recorrido = 0
    if len(lista_reales) == 0:
        recorrido = 0.0

    else:
        maximo = max_reales(lista_reales)
        minimo = min_reales(lista_reales)

        recorrido = maximo - minimo

        # print(recorrido)
        return recorrido



# 6
def media_reales(lista_reales):
    suma = suma_reales(lista_reales)
    media = suma / len(lista_reales)

    # print(suma)
    # print(len(lista_reales))
    # print(media)

    return round(media,2)


# 7
def variancia(lista_reales):
    n = len(lista_reales)
    if n <= 1:
        print("Solo se puede calcular la varianza si hay mas de un elemento en la lista")
    else:
        media = media_reales(lista_reales)

        suma_total = 0
        for valor in lista_reales:
            suma_total += (valor - media) **2 #Cuadrado

        #print(suma_total)

        variancia = suma_total / (n-1)

        return round(variancia,4)

# 1
print("Lista: "+ str(secuencia_reales()))

# 2
print("suma lista reales: " + str(suma_reales(lista_reales)))

# 3
print("Valor maximo en lista: " + str(max_reales(lista_reales)))

# 4
print("Valor minimo en lista: " + str(min_reales(lista_reales)))

# 5
print("Recorrido de la lista: "+ str(recorrido_reales(lista_reales)))
# 6
print("Valor medio de la lista: "+ str(media_reales(lista_reales)))

# 7
print("La varianza de la lista: "+ str(variancia(lista_reales)))
