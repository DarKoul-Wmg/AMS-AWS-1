"""Exercici 3:
Feu un programa que permetri entrar paraules fins a la paraula 'fi', un cop finalitzada l'entrada de dades ha d'indicar
si hi ha alguna paraula repetida."""


def buscar_repetidas(palabras):
    palabras_set = set()
    for palabra in palabras:
        palabra_lower = palabra.lower()
        if palabra_lower == 'fi':
            return False
        if palabra_lower in palabras_set:
            return True
        palabras_set.add(palabra_lower)
    return False


print("Introduce palabras. Escribe 'fi' para terminar.")

palabras = []
while True:
    palabra = input("> ")
    palabra_lower = palabra.lower()
    if palabra_lower == 'fi':
        break
    palabras.append(palabra)

if buscar_repetidas(palabras):
    print("Se han encontrado palabras repetidas.")
else:
    print("No se han encontrado palabras repetidas.")
