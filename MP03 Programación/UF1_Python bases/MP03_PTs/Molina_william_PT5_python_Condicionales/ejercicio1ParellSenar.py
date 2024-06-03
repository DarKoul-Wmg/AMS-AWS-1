#Feu un programa que llegeixi un número sencer, i ens digui si és parell o senar.
print("Introduir un número sencer")

num = int(input())

p = 'Parell'
s = 'Senar'

if num % 2 == 0 :

    num = p

else:
    num = s

print("El número es " + num )
