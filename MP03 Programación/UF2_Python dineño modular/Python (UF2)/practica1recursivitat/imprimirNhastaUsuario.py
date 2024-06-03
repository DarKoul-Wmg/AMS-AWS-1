def imprimir_numeros(n):
    if n == 1:
        print(n)
    else:
        imprimir_numeros(n - 1)
        print(n)


numero = int(input("Introduce un número: "))
print("Imprimiendo valores desde 1 hasta", numero, ":")
imprimir_numeros(numero)
