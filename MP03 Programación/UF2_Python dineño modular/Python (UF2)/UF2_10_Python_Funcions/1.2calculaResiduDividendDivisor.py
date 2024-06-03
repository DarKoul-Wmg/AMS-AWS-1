# 1.2) Función para calcular el residuo de una división
"""Feu una funció “calculaResidu” a la que passem per paràmetre el dividend i el divisor, i torna com a resultat
el residu de la divisió. calculaResidu( dividend, divisor)"""


def calcula_residuo(dividendo, divisor):
    return dividendo % divisor


dividendo = 10
divisor = 3
residuo = calcula_residuo(dividendo, divisor)
print("Residuo de la división:", residuo)
