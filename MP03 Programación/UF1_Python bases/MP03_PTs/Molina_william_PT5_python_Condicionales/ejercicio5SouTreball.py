# 5) En una empresa necessiten un petit programa que permeti calcular l’import que han de
# pagar als treballadors. Els pagaments es fan de forma setmanal. Per a cada assalariat es
# recullen via teclat les següents dades:

# · Número d’hores setmanals treballades a la setmana
# · Preu per hora ( és diferent per a cada treballador )
# Es considera que un treballador comença a fer hores extres a partir de la hora 35. Les hores
# extres es paguen un 50% més que les hores normals.
# El programa ha d’imprimir per pantalla l’import final, tenint en compte el preu hora indica t i si
# hi ha hores extres o no.
print("A continuació posa les dades sol·licitades per poder calcular l'import a pagar ")

print("Posa les hores treballades")
h = int(input())

print("Introdueix el teu preu per hora")
p = int(input())

if h <= 35:
    print('Import a cobrar es ' + str(h * p))

else:
    hx = h - 35
    h = h - hx
    print("L'import a cobrar per les hores normals: " + str(h * p))
    print("L'import per hores extra es: " + str (hx * (p * 1.5)))
    print("Cobres un total de: " + str((h*p) + (hx * (p * 1.5))))

