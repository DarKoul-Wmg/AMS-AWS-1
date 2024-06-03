"""Exercici 4:
Crear un mòdul per validació de contrasenyes. L'esmentat mòdul, haurà de complir amb els
següents criteris d'acceptació:
- La contrasenya ha de tenir un mínim de 8 caràcters.
- Una contrasenya ha de tenir lletres minúscules, majúscules, números i almenys 1
  caràcter no alfanumèric.
- La contrasenya no pot contenir espais en blanc.
- Contrasenya vàlida, retorna True.
- Contrasenya no vàlida, retorna el missatge "La contrasenya triada no és segura"."""

import re


def validar_contrasenya(contrasenya):
    # Comprobando la longitud mínima de la contraseña.
    if len(contrasenya) < 8:
        return "La contrasenya ha de tenir un mínim de 8 caràcters"

    # Comprobando si la contraseña contiene letras minúsculas, mayúsculas, números y al menos un carácter no
    # alfanumérico.
    if not re.search("[a-z]", contrasenya) or \
            not re.search("[A-Z]", contrasenya) or \
            not re.search("[0-9]", contrasenya) or \
            not re.search("[^a-zA-Z0-9]", contrasenya):
        return "La contrasenya triada no és segura"

    # Comprobando si la contraseña contiene espacios en blanco.
    if " " in contrasenya:
        return "La contrasenya no pot contenir espais en blanc"

    # La contraseña cumple con todos los criterios, es válida
    return True
