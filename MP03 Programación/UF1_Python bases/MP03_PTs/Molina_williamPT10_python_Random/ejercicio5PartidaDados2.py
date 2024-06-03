import random
punt_anna = 9
punt_bernat = 9

while punt_anna > 0 and punt_bernat > 0:

    dau = random.randint(1,6)
    print("Resultado lanzamiento:",dau)

    if dau in [1, 3, 5]: #Impar
        punt_bernat -= dau
        punt_anna +=  dau


    else: #Par
        punt_bernat +=  dau
        punt_anna -= dau

    print(f"Puntos restantes, Bernat: {punt_bernat}, Anna: {punt_anna}")
    print("")

if punt_bernat <= 0:
    print("HA GANADO ANNA!!!!")
    print(f"Con:{punt_anna} pts")

else:
    print("HA GANADO BERNAT!!!!")
    print(f"Con:{punt_bernat} pts")

