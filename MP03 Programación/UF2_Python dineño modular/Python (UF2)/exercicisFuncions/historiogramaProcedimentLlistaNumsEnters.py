# Ejercicio 5
"""5. Definir un histograma procedimient() que tomi una llista de números enters i imprimeixi un histograma en la pantalla.
    Exemple: procedimient([4, 9, 7]) hauria d’imprimir:
        ****
        *********
        *******"""


def procedimient(llista):
    for num in llista:
        print("*" * num)


procedimient([2, 4, 6])
print("\n")
procedimient([6, 8, 10])
print("\n")
procedimient([12, 14, 16])
