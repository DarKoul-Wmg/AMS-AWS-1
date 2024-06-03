"""Exercici 2:
Exercici 2:
Feu una funció que indiqui quina posició ocupa una lletra en una paraula sense usar la funció string.find"""


# Contando desde 0:
def buscar_posicion_letra(palabra, letra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            return i
    # Devolver -1 si la letra no está en la palabra:
    return -1


palabra = "Hola"
letra = "o"
posicion = buscar_posicion_letra(palabra, letra)
if posicion != -1:
    print(f"La letra '{letra}' aparece en la posición {posicion} de la palabra '{palabra}'.")
else:
    print(f"La letra '{letra}' no está en la palabra '{palabra}'.")


# Contando desde 1:
def buscar_posicion_letra(palabra, letra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            return i + 1
    # Devolver 0 si la letra no está en la palabra:
    return 0


palabra = "Hola"
letra = "o"
posicion = buscar_posicion_letra(palabra, letra)
if posicion != 0:
    print(f"La letra '{letra}' aparece en la posición {posicion} de la palabra '{palabra}'.")
else:
    print(f"La letra '{letra}' no está en la palabra '{palabra}'.")
