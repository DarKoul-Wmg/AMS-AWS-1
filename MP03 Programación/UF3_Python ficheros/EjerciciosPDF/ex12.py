union = open("1a100.txt","w+")
senars = open("11senars.txt", "r")
parells = open("11parells.txt", "r")

senars.seek(0)
parells.seek(0)

for i in range(1, 101):
    if i % 2 == 0:
        union.write(str(parells.seek(i))+"\n")
    else:
        union.write(str(senars.seek(i))+"\n")

for element in union:
    print(element)
