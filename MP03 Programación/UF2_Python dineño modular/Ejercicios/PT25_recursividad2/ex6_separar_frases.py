def separar_frase(frase):
    resultado = ""
    if len(frase) == 1:
        resultado += frase[0]
        print(resultado)
    else:
        if frase[0].isspace():
            print(resultado)
        resultado += frase[0]
        return resultado + separar_frase(frase[1:])

.
frase = "Tres tristes tigres"
separar_frase(frase)
