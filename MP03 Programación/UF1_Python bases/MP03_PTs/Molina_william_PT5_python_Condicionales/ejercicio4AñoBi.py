# 4) Un programa ha de llegir un any pel teclat i ens ha de dir si és any de traspàs o no.
print("Introdueix l'any")
a = int(input())

if a%4 == 0 and a%100 == 0 and a%400 == 0:
    print("Es bisiesto")

else: print("No es bisiesto")
