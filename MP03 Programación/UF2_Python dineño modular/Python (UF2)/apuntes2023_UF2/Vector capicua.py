# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ——————————————————————————————————————————— PROGRAMAR UNA FUNCIÓ RECURSIVA ———————————————————————————————————————————
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
ESQUEMA DE RAZONAMIENTO
1. Obtener un resultado parcial tratando una parte de los datos y...
2. Llamar a la misma función para obtener "el resto" del resultado tratando el resto de los datos.
(Para dar el resultado habrá que combinar de la manera adecuada el resultado obtenido en los pasos 1 y 2).
3. Determinar la condición que interrumpe la recursión. ¡Imprescindible!

PRIMERA APROXIMACIÓN:
1. Si coinciden los elementos primero y último, de momento, el vector es palíndromo.
2. A ver si es palíndromo el vector sin los elementos de los extremos.
3. ¿?
"""
from colorama import Fore


def vectorcapicua(vector):
    print(Fore.LIGHTYELLOW_EX + "He recibido el siguiente vector", vector)
    if not vector:
        return True
    elif vector[0] != vector[len(vector)-1]:
        print(Fore.LIGHTRED_EX + "Devuelvo lo siguiente:")
        return False
    else:
        print(Fore.LIGHTWHITE_EX + "Devuelvo lo que me diga la función sobre el vector", vector[1:len(vector)-1])
        return vectorcapicua(vector[1:len(vector)-1])


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
v1 = [1, 2, 3, 4]
v2 = [1, 2, 2, 1]
v3 = [1, 2, 3, 4, 5]
v4 = [1, 2, 4, 3, 5, 6]
print(vectorcapicua(v1))
print(vectorcapicua(v2))
print(vectorcapicua(v3))
print(vectorcapicua(v3))
print(vectorcapicua(v4))
