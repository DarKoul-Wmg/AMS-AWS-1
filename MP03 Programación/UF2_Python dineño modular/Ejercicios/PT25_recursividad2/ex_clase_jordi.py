def elementocomun(string1,string2):
    resultado = ""

    if len(string1) == 0:
        return resultado

    else:
        resultado += elementocomun(string1[1:],string2)
        if string1[0] in string2:
            if string1[0] not in resultado:
                resultado += string1[0]
        return resultado 


string1 = "casa"
string2 = "abracadabra"

print(elementocomun(string1,string2))
