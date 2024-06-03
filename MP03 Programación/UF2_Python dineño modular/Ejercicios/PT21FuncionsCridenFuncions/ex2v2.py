def desglossar_quantitat(euros):
    billets = [500, 200, 100, 50, 20, 10, 5]
    monedes = [2, 1]

    for billet in billets:
        quocient = euros // billet
        if quocient > 0:
            print(f"{quocient} {'bitllets' if billet > 1 else 'bitllet'} de {billet} euros.")
            euros %= billet #residuo de la operación al dividir los billetes es el dinero restante

    for moneda in monedes:
        quocient = euros // moneda
        if quocient > 0:
            print(f"{quocient} {'monedes' if moneda > 1 else 'moneda'} de {moneda} euro.")
            euros %= moneda

# Exemple d'ús
quantitat = 434
desglossar_quantitat(quantitat)
