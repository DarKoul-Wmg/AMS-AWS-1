def secuencia_curiosa(n):
    # Caso base: cuando n es igual a 1, imprime la primera línea de la secuencia.
    if n == 1:
        print("1 1")
    else:
        # Llama recursivamente a la función con n-1 para imprimir las líneas anteriores.
        secuencia_curiosa(n - 1)

        # Imprime el número actual (n) seguido de un espacio, sin pasar a la siguiente línea.
        print(n, end=" ")

        # Imprime los números en orden ascendente desde 1 hasta n (inclusive).
        for i in range(1, n + 1):
            print(i, end="")

        # Imprime los números en orden descendente desde n-1 hasta 1.
        for i in range(n - 1, 0, -1):
            print(i, end="")

        # Salto de línea para pasar a la siguiente línea de la secuencia.
        print()


# Llama a la función con n=8 para generar la secuencia hasta el nivel 8.
secuencia_curiosa(8)
