fpar = open("11parells.txt", "a+")
fsenar = open("11senars.txt", "a+")

for num in range(1,101):
    if num %2 == 0:
        fpar.write(str(num)+"\n")

    else:
        fsenar.write(str(num)+"\n")

fpar.close()
fsenar.close()
