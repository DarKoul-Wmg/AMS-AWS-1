def es_palindrom(frase):
    # Lista de signos de puntuación a eliminar.
    llista_signes_puntuacio = [" ", ".", ",", "!", "'", ":"]

    # Eliminar espacios y signos de puntuación.
    frase_sense_espais = ''.join(caracter.lower() for caracter in frase if caracter not in llista_signes_puntuacio)

    # Verificar si la frase sin espacios y signos de puntuación es un palíndromo.
    return frase_sense_espais == frase_sense_espais[::-1]

# Ejemplos de uso:
frases = [
    "Madam, I'm Adam.",
    "A man, a plan, a canal: Panama!",
    "Amore, Roma.",
    "Emu love volume.",
    "God lived as a devil dog.",
    "Is it I, It is I!",
    "Red rum, sir, is murder.",
    "Miau",
    "Mim"
]

for frase in frases:
    resultat = es_palindrom(frase)
    print(f'"{frase}": {resultat}')
