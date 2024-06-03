import math
# #4. Escriure un programa que li pregunti a l’usuari una quantitat de
# diners, una tassa d’interès i un número de anys. El programa haurà
# de mostrar com a resultat la quantitat de diners a pagar.
# La fórmula a utilitzar és:
# Cn = C * (1 + x/100) ^ n
# A on C és el capital inicial, x és la tassa d’interès i n és el número
# d’anys a calcular.

print("Introduïu a continuació les seguents dades solicitades per poder calcular la quantitat de diners a pagar ")

print("Introduir capital inicial ")
C = float(input())

print("Introduir la tassa d'interés ")
x = float(input())

print("Introduir el número d'anys a calcular ")
n = float(input())

Cn = C * math.pow(1 + x/100, n)

print("La cuantitat de diners a pagar es "+ str(Cn))
