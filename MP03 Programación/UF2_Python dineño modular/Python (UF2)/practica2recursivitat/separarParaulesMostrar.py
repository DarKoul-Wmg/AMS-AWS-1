def separar_palabras(frase):
    if ' ' not in frase:
        print(frase)
    else:
        palabra, resto = frase.split(' ', 1)
        print(palabra)
        separar_palabras(resto)


frase = "Hola mundo, ¿cómo estás?"
print("Separando las palabras de la frase:")
separar_palabras(frase)
