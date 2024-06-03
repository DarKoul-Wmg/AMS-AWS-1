"""Exercici 1:
Crearem un paquet anomenat matemàtiques i a dintres un mòdul anomenat operacions_basiques.py que contindrà les funcions:
- sumar -> Funció que suma els dos paràmetres i retorna el resultat.
- restar -> Funció que resta dels dos paràmetres i retorna el resultat.
- multiplicar -> Funció que multiplica els paràmetres i retorna el resultat.
- dividir -> Funció que divideix els paràmetres (numerador, denominador) i retorna el resultat. Llança una excepció en
  cas de divisió per zero. El codi d'aquesta excepció mostrarà el missatge 'ERROR: No es pot dividir per zero' i
  llançarà una excepció del tipus ZeroDivisionError."""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(numerador, denominador):
    if denominador == 0:
        raise ZeroDivisionError("ERROR: No es pot dividir per zero!")
    return numerador / denominador
