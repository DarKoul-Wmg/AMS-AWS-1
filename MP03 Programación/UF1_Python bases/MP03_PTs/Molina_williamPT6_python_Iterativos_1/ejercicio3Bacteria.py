#Valors inicials

mort = 10000000
tempRep = 3
bact = 1
tempTot = 0

#Bucle
while bact <= mort:
    bact *= 2 #Duplicació per cicle
    tempTot += tempRep #Suma de min per cada bucle

temp = tempTot / 60

print("La bacteria ha trigat: " + str(tempTot) + " hores en assolir la xifra mortal.")
