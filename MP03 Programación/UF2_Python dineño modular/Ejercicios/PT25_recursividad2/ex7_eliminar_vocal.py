def eliminar_vocal_frase(frase):
    resultado =""
    if len(frase) == 0:
        return resultado
    else:
        if frase[0].lower() == "a" or frase[0].lower() == "e" or frase[0].lower() == "i" or frase[0].lower() \
                == "o" or frase[0].lower() == "u":
            return resultado + eliminar_vocal_frase(frase[1:])
        else:

            resultado += frase[0]
            return resultado + eliminar_vocal_frase(frase[1:])



frase = "Tres tristes tigres"
print(eliminar_vocal_frase(frase))
