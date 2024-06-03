#Contador per calcular els multiples de 7
cont = 0

for num in range(1, 1001): #Per introduïr dintre del rang el num 1000, +1
    if num % 7 == 0:
        cont += 1

print("Entre els números 1 i 1000 hi ha "+ str(cont) + " multiples de 7.")
