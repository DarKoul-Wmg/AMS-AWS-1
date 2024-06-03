# 1.7) Función para convertir un carácter a mayúscula si es una letra
"""Feu una funció “aMajuscula” que, donat un caràcter qualsevol:
    a) Ens el torni convertit a majúscula en el cas de ser una lletra
    b) Eel deixi igual si no és una lletra.
                        aMajuscula(caracter)                      """


# No recursiva:
def aMajuscula(caracter):
    if caracter.isalpha():
        return caracter.upper()
    else:
        return caracter


print(aMajuscula('a'))
print(aMajuscula('1'))


# Recursiva:
def aMajusculaRecursiva(caracter):
    if len(caracter) == 1:
        if 'a' <= caracter <= 'z':
            return chr(ord(caracter) - 32)
        else:
            return caracter
    else:
        return aMajusculaRecursiva(caracter[0]) + aMajusculaRecursiva(caracter[1:])


print(aMajusculaRecursiva('a'))
print(aMajusculaRecursiva('1'))
