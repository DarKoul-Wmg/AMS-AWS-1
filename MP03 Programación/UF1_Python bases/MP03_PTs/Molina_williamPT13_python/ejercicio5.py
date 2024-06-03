k = int(input("introdueix un valor entre 0 i 50"))
lista = [1,34,2,33,7,8,21,44,50,14,25,19,37,41]
menorK = []
superK = []
igualK = []
multipleK = []

for num in lista:
    if num < k:
        menorK.append(num)
    elif num > k:
        superK.append(num)
    else:
        igualK.append(num)

print("Numeros menores que k: ")
for num in menorK:
    print(num)

print("\n")

print("Numeros mayor que k: ")
for num in superK:
    print(num)

print("\n")

print("Numero igual que k: ")
for num in igualK:
    print(num)

print("\n")

print("Multiples de k: ")
for num in lista:
    if num % k ==0:
        print(num)

print("\n")
