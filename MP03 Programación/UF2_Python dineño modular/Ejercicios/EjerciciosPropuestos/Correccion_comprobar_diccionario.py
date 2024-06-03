diccionario = {"clave1": 2, "clave2": "valor2", "clave3": [1, "valor3", 7]}

def comprobarDiccionario(clave,valor,diccionario):
    if clave not in diccionario:
        print("Clave no existe en diccionario")
        return False

    else:

        if type(diccionario[clave]) == int and diccionario[clave] == valor:
            print("Valor coincide como int")
            return True

        elif type(diccionario[clave]) == str and type(valor) == str and valor in diccionario[clave]:
            print("Valor coincide como str")
            return True

        elif type(diccionario[clave]) == list and valor in diccionario[clave]:
            print("Valor dentro de lista")
            return True

        else:
            print("VALOR NO COINCIDENTE")
            return False

print(comprobarDiccionario("clave3",7,diccionario))