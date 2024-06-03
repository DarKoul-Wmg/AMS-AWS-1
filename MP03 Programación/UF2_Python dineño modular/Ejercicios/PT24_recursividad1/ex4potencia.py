def potencia(x,y):
    resultado = 1
    if y == 0:
        return resultado
    else:
        resultado = x * potencia(x,y-1)
        return resultado


x =8
y =4
print(potencia(x,y))
