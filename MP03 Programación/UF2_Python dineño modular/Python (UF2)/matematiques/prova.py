"""Exercici 1:
Crearem un paquet anomenat matemàtiques i a dintres un mòdul anomenat operacions_basiques.py que contindrà les funcions:
- sumar -> Funció que suma els dos paràmetres i retorna el resultat.
- restar -> Funció que resta dels dos paràmetres i retorna el resultat.
- multiplicar -> Funció que multiplica els paràmetres i retorna el resultat.
- dividir -> Funció que divideix els paràmetres (numerador, denominador) i retorna el resultat. Llança una excepció en
  cas de divisió per zero. El codi d'aquesta excepció mostrarà el missatge 'ERROR: No es pot dividir per zero' i
  llançarà una excepció del tipus ZeroDivisionError."""
from matematiques import operacions_basiques
a = 10
b = 2

print("Suma:", operacions_basiques.sumar(a, b))
print("Resta:", operacions_basiques.restar(a, b))
print("Multiplicación:", operacions_basiques.multiplicar(a, b))

try:
    print("División:", operacions_basiques.dividir(a, b))
except ZeroDivisionError as e:
    print(e)
