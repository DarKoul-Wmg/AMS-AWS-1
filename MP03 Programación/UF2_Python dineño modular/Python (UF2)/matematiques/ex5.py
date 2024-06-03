""" Exercici 5:
Crear un mòdul que sol·liciti a l'usuari l'ingrés d'un nom d'usuari i contrasenya i que els validi utilitzant els mòduls
generats en els dos exercicis anteriors.
Ajuda: per comptar la quantitat de caràcters d'una cadena, en Python s'utilitza la funció incorporada: len (cadena)."""
from ex3 import validar_nom_usuari
from ex4 import validar_contrasenya


def validar_credenciales():
    nom_usuari = input("Introdueix el nom d'usuari: ")
    contrasenya = input("Introdueix la contrasenya: ")
    resultado_nom_usuari = validar_nom_usuari(nom_usuari)
    resultado_contrasenya = validar_contrasenya(contrasenya)

    if resultado_nom_usuari == True and resultado_contrasenya == True:
        print("Nom d'usuari i contrasenya vàlids.")
    else:
        print("\nError:", end="")
        if resultado_nom_usuari != True:
            print("\n- " + resultado_nom_usuari)
        if resultado_contrasenya != True:
            print("- " + resultado_contrasenya)


validar_credenciales()
