# Ejercicio 4
"""4. Definir una funció superposicio() que tomi dos llistes i retorni true si tenen al menys 1 membre en comú o retorni
    false de lo contrari."""


def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False


print(superposicio([1, 2, 3, 4], [4, 5, 6, 7]))
print(superposicio([10, 20], [30, 40]))
print(superposicio([100, 200], [200, 300]))
