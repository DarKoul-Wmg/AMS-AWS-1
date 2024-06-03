def frase_escala(frase):
    if frase:
        frase_escala(frase[:-1])
        print(frase)




frase = "Benvinguts"
frase_escala(frase)


# for i in range(len(frase)):
#      print(frase[:i])
