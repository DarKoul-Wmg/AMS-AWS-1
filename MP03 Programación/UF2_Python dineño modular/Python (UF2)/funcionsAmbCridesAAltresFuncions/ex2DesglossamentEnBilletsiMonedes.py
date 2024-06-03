"""Exercici 2:
Realitza un programa que calculi el desglossament en bitllets i monedes d’una quantitat exacta d’euros. Hi ha bitllets
de 500, 200, 100, 50, 20, 10 i 5 € i monedes de 2 i 1 €.
Per exemple, si volem conèixer el desglossi de 434 €, el programa mostrarà per pantalla el següent resultat:
    2 bitllets de 200 euros.
    1 bitllet de 20 euros.
    1 bitllet de 10 euros.
    2 monedes de 2 euros.
NOTA: Per fer el desglossament es comença per calcular la divisió entera entre la quantitat i 500 (el valor de la moneda
més gran): 434 entre 500 dona 0, perquè no hi ha bitllets de 500 € en el desglossament; a continuació, es divideix la
quantitat 434 entre 200, el quocient és 2 i el residu 34, així que en el desglossament hi ha 2 bitllets de 200 €;
dividim a continuació 34 entre 100 i com dona 0 no hi ha cap bitllet de 100 € en el desglossament; com el residu de
l'última divisió és 34, passem a dividir 34 entre 20 i veiem que el desglossament inclou un bitllet de 20 € i encara ens
falten 14 € per desglossar... )"""


def desglosar_euros(cantidad):
    # Definir los valores de los billetes y monedas.
    valores = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    nombres = ["billete de 500 euros", "billete de 200 euros", "billete de 100 euros",
               "billete de 50 euros", "billete de 20 euros", "billete de 10 euros",
               "billete de 5 euros", "moneda de 2 euros", "moneda de 1 euro"]

    # Inicializar el índice para recorrer los valores.
    indice = 0

    # Calcular el desglose de la cantidad.
    while cantidad > 0:
        billete_o_moneda = cantidad // valores[indice]
        cantidad %= valores[indice]
        if billete_o_moneda > 0:
            print(f"{billete_o_moneda} {nombres[indice]}.")
        indice += 1


cantidad_euros = int(input("Introduce la cantidad de euros.\n> "))
print("Desglose de la cantidad de euros:")
desglosar_euros(cantidad_euros)
