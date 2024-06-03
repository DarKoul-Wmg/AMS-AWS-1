def capicua(frase):
    signes = [" ",".",",","!","'"]
    if len(frase) <= 1:
        return True
    else:
        if frase[0].lower() == frase[-1].lower():
            return capicua(frase[1:-1])

        if frase[0] in signes:
            return capicua(frase[1:])
        if frase[-1] in signes:
            return capicua(frase[:-1])
        else:
            return False



frase = "Amore, Roma"
#frase = "Madam, I'm Adam"
#frase = "Is it I, It is I!"
print(capicua(frase))
