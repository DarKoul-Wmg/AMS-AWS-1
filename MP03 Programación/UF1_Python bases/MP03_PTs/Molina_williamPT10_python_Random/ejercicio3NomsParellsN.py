import random
n = int(input("Dime un numero hasta el que quieres que genere una secuencia:"))
print("")
print("Los numeros pares generados son:")
for num in range(n):
    x = random.randrange(0,n,2)
    print(str(x).rjust(4))


