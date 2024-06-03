# 2. Producto de dos números de manera recursiva
def producto(x, y):
    if y == 0:
        return 0
    else:
        return x + producto(x, y - 1)


print("Producto de 2 · 3 =", producto(2, 3))