# 2) Un instal·lador de xarxa cobra segons hores treballades i metres de cable instal·lats.
# Assumirem que el preu per hora són 30€ l’hora i el preu per metre del cable és 0,5€.
# Aquestes dues quantitats són fixes (CONSTANTS).
# El programa ens haurà de demanar:
# · les hores treballades
# · el número de metres instal·lats
# i ens traurà per pantalla:
# • el preu brut és ....
# • el preu amb IVA és ....
print("Introduir hores treballades:")
Ht = float(input())
print("Introduir metres de cable utilitzats:")
Mc = float(input())

Pb = Ht * 30 + (Mc * 0.5)
Piv =   Pb + (Pb * 0.21)

print('\n        \n')
print("El preu en brut es: " + str(Pb))
print("El preu amb IVA es: " + str(Piv))
