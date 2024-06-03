# Ejercicio 7
"""7. Escriure una funcio sum() i una funció multip() que sumen i multipliquin respectivament tots els números d’una
    llista. Per exemple: sum([1,2,3,4]) hauria de tornar 10 i multip([1,2,3,4]) hauria de tornar 24."""


def sum(llista):
    suma = 0
    for num in llista:
        suma += num
    return suma


print(sum([13, 11, 21]))
print(sum([20, 11, 21]))
print(sum([6, 7, 2004]))
