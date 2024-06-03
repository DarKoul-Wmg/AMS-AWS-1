# 2) Programar un algoritme recursiu que permeti sumar els dígits d’un número.

def suma_digits(numero):
    """ Funció recursiva per a la suma dels dígits d'un número.
        :param numero: El número del qual volem sumar els dígits.
        :return: La suma dels dígits. """
    # Cas base: si el número és un dígit, la suma és el propi número.
    if numero < 10:
        return numero

    # Pas recursiu: suma l'últim dígit i crida la funció amb el número sense aquest dígit.
    return numero % 10 + suma_digits(numero // 10)


# Exemple d'ús.
numero = 355
resultat = suma_digits(numero)

# Imprimim el resultat.
print(f"La suma dels dígits de {numero} és {resultat}")
