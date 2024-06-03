# 1.5) Función para verificar si un carácter es un dígito
"""Creeu una funció “esDigit” que, donat un caràcter qualsevol, ens digui si és numèric o no. La funció rep un
paràmetre que representarà un únic caràcter, i retorna un valor entero ( 1 si el caràcter és un número, 0 si
no ho és).          esDigit(caracter)"""


def es_digit(caracter):
    if len(caracter) == 1:
        return 1 if caracter.isdigit() else 0
    else:
        return es_digit(caracter[0])


caracter = "5"
if es_digit(caracter):
    print(f"'{caracter}' es un dígito.")
else:
    print(f"'{caracter}' no es un dígito.")
