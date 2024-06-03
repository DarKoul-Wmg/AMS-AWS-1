def alfabetica(palabra):
    lista_alfabetica = []

    for caracter in palabra:
        lista_alfabetica.append(caracter)
    #print(lista_alfabetica)

    for i in range(len(lista_alfabetica)-1):
        for j in range(len(lista_alfabetica)-1-i):
            if lista_alfabetica[j] > lista_alfabetica[j+1]:
                opc = lista_alfabetica[j]
                lista_alfabetica[j] = lista_alfabetica[j+1]
                lista_alfabetica[j+1] = opc

    #print(lista_alfabetica)
    palabra_alfabetica = ''
    for letra in lista_alfabetica:
        palabra_alfabetica += letra
    #print(palabra_alfabetica)

    if palabra == palabra_alfabetica:
        print("La palabra esta en orden alfabetico")

    else:
        print("La palabra no se encuentra en orden alfabetico")


palabra = input("Introduce una palabra:\n")
alfabetica(palabra)
