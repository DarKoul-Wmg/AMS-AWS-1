def producte(x,y):
    resultado = 0

    if y == 0:
        return resultado

    else:
        resultado += x
        return resultado + producte(x,y-1)

x = 2
y = 3

print(producte(x,y))
