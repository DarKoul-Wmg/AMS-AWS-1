""" Exercici 3:
Crear un mòdul per validació de noms d'usuaris. L'esmentat mòdul, haurà de complir amb els
següents criteris d'acceptació:
- El nom d'usuari ha de contenir un mínim de 6 i un màxim de 12.
- El nom d'usuari ha de ser alfanumèric.
- Nom d'usuari amb menys de 6 caràcters, retorna el missatge "El nom d'usuari ha de
contenir almenys 6 caràcters".
- Nom d'usuari amb més de 12 caràcters, retorna el missatge "El nom d'usuari no pot
contenir més de 12 caràcters".
- Nom d'usuari amb caràcters diferents als alfanumèrics, retorna el missatge "El nom
d'usuari pot contenir només lletres i números".
- Nom d'usuari vàlid, retorna True. """

import re
# 1ª VERSIÓN:


def validar_nom_usuari(nom_usuari):
    # Valida el nombre de usuario según los criterios especificados.
    if len(nom_usuari) < 6:
        return "El nom d'usuari ha de contenir almenys 6 caràcters."
    elif len(nom_usuari) > 12:
        return "El nom d'usuari no pot contenir més de 12 caràcters."
    elif not re.match("^[a-zA-Z0-9]*$", nom_usuari):
        return "El nom d'usuari pot contenir només lletres i números."
    else:
        return True


# 2ª VERSIÓN:


def validar_nom_usuari2(nom_usuari2):
    if len(nom_usuari2) < 6:
        return "El nom d'usuari ha de contenir almenys 6 caràcters."
    elif len(nom_usuari2) > 12:
        return "El nom d'usuari no pot contenir més de 12 caràcters."
    elif not nom_usuari2.isalnum():
        return "El nom d'usuari pot contenir només lletres i números."
    else:
        return True
