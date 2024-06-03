# 1.6) Función para determinar si un carácter es una letra o no
"""Creeu una funció “esLletra” que, donat un caràcter qualsevol, ens digui si és una lletra o no. La funció rep un
paràmetre, i retorna un valor enter (1 si és una lletra, 0 si no ho és)."""


# No recursiva:
def esLletra(caracter):
    return 1 if caracter.isalpha() else 0


print(esLletra("a"))
print(esLletra("1"))


# Recursiva:
def esLletraRecursiva(caracter):
    if len(caracter) == 1:
        return 1 if 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z' else 0
    else:
        return esLletraRecursiva(caracter[0]) if 'a' <= caracter[0] <= 'z' or 'A' <= caracter[0] <= 'Z' else 0


print(esLletraRecursiva("a"))
print(esLletraRecursiva("1"))