# 3) Un programa llegirà tres números per teclat. La sortida del programa serà treure per
# pantalla si l’usuari ha introduït aquests números per ordre de menor a major o no. p.ex. si
# l’usuari entra 1,4,6 el programa dirà “ números en ordre” si l’usuari entra 5,7,3 el programa
# dirà “ números desordenats”

print("Introduir tres numeros: ")
print("Primer numero: ")
num1 = int(input())
print("Segon numero: ")
num2 = int(input())
print("Tercer numero: ")
num3 = int(input())

if num1 < num2 < num3 :
    print("Números en ordre")

else:
    print("Números desordenats")

