import math
# Escriure un programa que converteixi un valor donat en graus
# Fahrenheit a graus Celsius. La fórmula de conversió és:
# F = 9/5 * C + 32
print("Introdueix un valor en graus Fahrenheit: ")
F = float(input())

C = float((5/9) * (F - 32))


print("El valor donat convertit en graus Celsius es: " + str(C))
