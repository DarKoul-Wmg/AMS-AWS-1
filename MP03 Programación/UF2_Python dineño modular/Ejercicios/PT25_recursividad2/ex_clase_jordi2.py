def unionsinrep(string1,string2):
    resultado = ""

    if len(string1) == 0 and len(string2) == 0:
        return resultado

    elif len(string1) == 0 and len(string2) !=0:
        resultado = unionsinrep(string1,string2[1:])

    elif len(string1) != 0 and len(string2) ==0:
        resultado = unionsinrep(string1[1:],string2)
    else:
        resultado = unionsinrep(string1[1:],string2[1:])

    if len(string1) > 0 and string1[0] not in resultado:
        resultado += string1[0]

    elif len(string2) > 0 and string2[0] not in resultado:
        resultado += string2[0]

    return resultado

string1 = "casa"
string2 = "abracadabra"

print(unionsinrep(string1,string2))

