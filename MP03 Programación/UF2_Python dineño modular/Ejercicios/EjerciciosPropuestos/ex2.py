diccionario = {"clave1": "valor1", "clave2": 2, "clave3": [1, "valor3", 7]}


def consultaDiccionario(clave, valor):
    if not clave in diccionario:
        print("Clave no encontrada")
        return False
    else:
        if len(diccionario[clave]) > 1:
            for elemento in diccionario[clave]:
                if elemento == int(valor):
                    return True
                if valor in elemento:
                    return True
        else:
            #if clave in diccionario.keys():
            if valor.isdigit():
                valor = int(valor)
                if valor == diccionario[clave]:
                    return True
                else:
                    return False

            elif valor in diccionario[clave]:
                return True

            else:
                return False



clave = input("Introduce una clave del diccioario:\n")
valor = input("Introduce el valor de la clave:\n")

resultadoBusqueda = consultaDiccionario(clave,valor)

print(resultadoBusqueda)


# dado un diccionario del tipo diccionario = {"clave1":"valor1","clave2":"valor2","clave3":"valor3", .....,"claveN":"valorN"}
# Crear una función que reciba como argumentos
# 1 claveX
# 2 Un valor "valorX" que podrá ser un string o un entero
# 3 el diccionario
#
# La función devolverá un booleano true o false. dependiendo de:
#
# Si la clave claveX no existe en el diccionario, devolverá False. Aparte imprimirá un mensaje informando de que no existe.
# Si la clave claveX existe en el diccionario:
#     si el valor asociado a la clave es un entero, devolverá True si el valor valorX es igual al valor asociado a la clave
#     si el valor asociado a la clave es un string, devolverá True si el valor valorX es está incluido en el valor asociado a la clave
#     si el valor asociado a la clave es una lista, devolverá True si el valor valorX es está en la lista asociada a la clave.
