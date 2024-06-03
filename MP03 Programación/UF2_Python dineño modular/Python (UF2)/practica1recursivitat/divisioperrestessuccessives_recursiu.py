# 1) Programar un algoritme recursiu que permeti fer la divisió per restes successives.

""" Funció recursiva per a la divisió utilitzant restes successives:
    :param divident: El nombre que es vol dividir.
    :param divisor: El nombre pel qual es vol dividir.
    :return: Quocient de la divisió. """

def divisio_recursiva(divident, divisor):
    # Cas base: si el divisor és igual a 0, no podem dividir.
    if divisor == 0:
        raise ValueError("No es pot dividir per zero")

    # Cas base: si el dividend és menor que el divisor, la divisió és 0.
    if divident < divisor:
        return 0

    # Cas recursiu: restem el divisor successivament fins que el dividend sigui menor que el divisor.
    return 1 + divisio_recursiva(divident - divisor, divisor)

# Exemple d'ús.
divident = 25
divisor = 5
resultat = divisio_recursiva(divident, divisor)

print(f"{divident} dividit per {divisor} és {resultat}")