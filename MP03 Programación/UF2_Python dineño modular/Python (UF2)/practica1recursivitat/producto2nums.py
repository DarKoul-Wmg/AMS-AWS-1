def producto_recursivo(a, b):
    if b == 0:
        return 0
    else:
        return a + producto_recursivo(a, b - 1)


a = 2
b = 3
print("Producto:", producto_recursivo(a, b))
