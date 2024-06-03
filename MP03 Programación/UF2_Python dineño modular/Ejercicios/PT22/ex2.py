
def posicion_letra(letra,palabra):
    if letra in palabra:
        posicion = 0

        for caracter in palabra:
            if not letra == caracter:
                posicion += 1

            elif letra == caracter:
                return posicion


palabra = input("Dime una palabra: ")
letra = input("Dime una letra a buscar: ")
resultado = posicion_letra(letra,palabra)

if resultado:
    print("La posicion de la letra es: "+ str(resultado))
else:
    print("La letra no se encuenta en la palabra dada")
