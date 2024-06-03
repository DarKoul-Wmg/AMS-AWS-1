ancho = int(input("Introduce la anchura: "))
alto = int(input("Introduce la altura: "))
for i in range(alto):
    for j in range(ancho):
        if (i == 0 or j == 0 or i == alto - 1 or j == ancho - 1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
