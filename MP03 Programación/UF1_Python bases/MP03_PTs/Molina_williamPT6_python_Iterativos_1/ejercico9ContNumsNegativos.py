numT = int(input("Quants números vols introduir? "))
cont = 0

for i in range(numT):
    num = int(input(f"Dona'm el número {str(i + 1)}: "))
    if num < 0:
        cont = cont + 1

print(f"Has escrit {cont} números negatius.")
