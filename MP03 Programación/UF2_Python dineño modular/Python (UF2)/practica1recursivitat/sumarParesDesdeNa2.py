def suma_pares(n):
    if n < 2:
        return 0
    elif n % 2 != 0:
        return suma_pares(n - 1)
    else:
        return n + suma_pares(n - 2)


N = 10
print("Suma de los enteros positivos pares desde", N, "hasta 2:", suma_pares(N))
