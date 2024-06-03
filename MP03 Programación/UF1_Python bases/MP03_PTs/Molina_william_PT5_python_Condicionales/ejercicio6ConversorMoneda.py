# 6) Volem fer un programa que serveixi per a convertir divises. En primer lloc el programa ens
# mostrarà el següent menú:
# Un cop l’usuari premi la tecla corresponent a l’opció que desitja, es mostrarà un missatge amb
# la conversió triada, i el programa demanarà la quantitat de la divisa d’origen. Final ment el
# programa calcularà la quantitat de divises de destí:
# NOTA: Useu les següents quantitats com a factors de conversió:
#Un euro = 115,998 Yens
#Un euro = 1,11894 Dolars

print("======================")
print("= 1.- Euro a Dolar")
print("= 2.- Euro a Yen")
print("= 3.- Dolar a Euro")
print("= 4.- Dolar a Yen")
print("= 5.- Yen a Euro")
print("= 6.- Yen a Dolar")
print("======================")
ex = input("= Escoge una opcion =")
print("======================")

#Un euro = 115,998 Yens
#Un euro = 1,11894 Dolars

# EURO - DOLAR
# def eurodolar(Euro):
#         return Euro * 1.11894
#
# # EURO - YEN
# def euroyen(Euro):
#      return Euro * 115.998
#
# # DOLAR - EURO
# def dolareuro(Dolar):
#      return Dolar / 1.11894
# # DOLAR - YEN
# def dolaryen(Dolar):
#     Euro = Dolar / 1.11894
#     return Euro * 115.998
#
# # YEN - EURO
# def yeneuro(Yen):
#     return Yen / 115.998
#
# # YEN - DOLAR
# def yendolar(Yen):
#     Euro = Yen / 115.998
#     return Euro * 1.111694

#=======================================================

if ex == "1":
    print("Quantitat d'Euros a canviar en Dòlars")
    Euro = float(input())
    Result = Euro * 1.11894
    print("La quantitat d'Euros introduïts són: " + str(Result) + " Dòlars")

elif ex == "2":
    print("Quantitat d'Euros a canviar en Yens")
    Euro = float(input())
    Result = Euro * 115.998
    print("La quantitat d'Euros introduïts són: " + str(Result) + " Yens")

elif ex == "3":
    print("Quantitat de Dòlars a canviar en Euros")
    Dolar = float(input())
    Result = Dolar / 1.11894
    print("La quantitat de Dòlars introduïts són: " + str(Result) + " Euros")

elif ex == "4":
    print("Quantitat de Dòlars a canviar en Yens")
    Dolar = float(input())
    Result = Dolar / 1.11894
    print("La quantitat de Dòlars introduïts són: " + str(Result) + " Yens")

elif ex == "5":
    print("Quantitat de Yens a canviar en Euros")
    Yen = float(input())
    Result = Yen / 115.998
    print("La quantitat de Yens introduïts són: " + str(Result) + " Euros")

elif ex == "6":
    print("Quantitat de Yens a canviar en Dòlars")
    Yen = float(input())
    Euro = Yen / 115.998
    Result = Euro * 1.111694
    print("La quantitat de Yens introduïts són: " + str(Result) + " Dòlars")

else:
    print("Error, comprovi que ha seleccionat una opció vàlida")
