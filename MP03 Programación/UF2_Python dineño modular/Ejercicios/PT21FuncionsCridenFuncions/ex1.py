#netejaPantalla() #Si situamos aqui la función, da error porque no esta definida

def tres_linies():
    for i in range(3):
        print("")

def nou_linies():

    for i in range(3):
        tres_linies()

def netejaPantalla():
    for i in range(25):
        print("")

def concatena_n_vegades(c,n):

    for i in range(n):
        print(c)



netejaPantalla()
tres_linies()
nou_linies()
concatena_n_vegades("hola",3)
