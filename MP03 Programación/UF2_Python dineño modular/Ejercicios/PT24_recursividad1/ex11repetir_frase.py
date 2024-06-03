def repetir_frase(rep, frase):
    if rep == 1:
        return frase
    else:
        return frase + repetir_frase(rep-1,frase)



rep = 3
frase = "Tres tristes tigres "
print(repetir_frase(rep,frase))
