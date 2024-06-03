def potencia(x, y):
    if y == 0:
        return 1
    else:
        return x * potencia(x, y - 1)


x = 2
y = 3
print("Potencia:", potencia(x, y))
