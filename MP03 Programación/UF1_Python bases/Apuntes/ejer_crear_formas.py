ancho = int(input("Introduce la anchura: "))
alto = int(input("Introduce la altura: "))
for i in range(alto):
    for j in range(ancho):
        if ((i == alto -j-1 and j == ancho - i-1 !=0) and (i == alto -j-1 and j == ancho - i-1 !=alto-1) or (i == j and j == i !=0) and (i == j and j == i !=ancho-1)):
            print("#",end="")
        else:
            print("+",end="") #Dibujar en la misma linea.
    print()
