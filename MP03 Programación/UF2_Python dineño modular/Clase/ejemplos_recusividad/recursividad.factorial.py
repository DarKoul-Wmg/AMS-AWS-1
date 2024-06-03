def funcionA(n):
    resultado = 1
    if n == 1:
        return resultado

    else:
        resultado = n*funcionA(n-1)
        return resultado


print(funcionA(5))

###debajo modo experto
#def funcionA(n):

    #if n == 1:
        #return 1

        #return n*funcionA(n-1)

#print(funcionA(5))