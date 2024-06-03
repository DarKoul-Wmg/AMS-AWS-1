def escalera(n):
    resultado = 1
    if n == 1:
        return resultado
    else:
        escalera(n-1)
    print(f"{str(n)}    {int('1'*n) * int('1'*n)} ")

n = 8
escalera(n)

#HACER funcion que imprima linea que le pasas n



def piramide(n):
    if n == 1:
        print("1 - 1")
        return
    else:
        piramide(n-1)
    print("{} - {}".format(n,int("1"*n)*int("1"*n)))
piramide(n)
