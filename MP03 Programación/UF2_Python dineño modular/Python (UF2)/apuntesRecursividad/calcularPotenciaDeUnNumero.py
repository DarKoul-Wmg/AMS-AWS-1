# 1. Potencia de manera recursiva
def potencia(x, y):
    if y == 0:
        return 1
    else:
        return x * potencia(x, y - 1)
