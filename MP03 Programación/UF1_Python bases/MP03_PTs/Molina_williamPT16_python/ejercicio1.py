frase = input("Introduce una frase: ")

diccionario = {}

#variables para rastrear palabras
inicio_palabra = 0
fin_palabra = 0
len_palabra = 0

for letra in frase:
    if letra.isalpha():
        fin_palabra +=1
        len_palabra +=1

    elif len_palabra > 0:
        palabra = frase[inicio_palabra:fin_palabra]
        diccionario[palabra] = len_palabra
        len_palabra = 0
        inicio_palabra = fin_palabra + 1

#Para la ultima palabra

if len_palabra > 0:
    palabra = frase[inicio_palabra:]
    diccionario[palabra] = len_palabra

print(diccionario)
