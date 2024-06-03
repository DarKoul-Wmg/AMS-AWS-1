

def lista_palabras():
    lista_palabras = []
    lista_palabras_rep = []
    palabras_rep = 0
    while True:

        palabra = input("Introduce una palabra.\n Para acabar de introducir pon 'fi': ")
        if palabra == "fi":
            break
        else:
            if palabra in lista_palabras:
                palabras_rep += 1
                lista_palabras_rep.append(palabra)

            lista_palabras.append(palabra)
    return palabras_rep


print("\nNumero de palabras repetidas: "+ str(lista_palabras()))

