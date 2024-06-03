""" 6. Calcula los números combinatorios.
Definición y ejemplo de número combinatorio:
(m n) = m! / n!(m-n) con m => n
Para calcular un número combinatorio siempre podemos:
(7 5) = 7! / 5! x 2! = 7 x 6 x 5! / 5! x 2! = 42 / 2 =21

Triángulo de Tartaglia:
                    1 1
                   1 2 1
                  1 3 3 1
                 1 4 6 4 1

                (1 0) (1 1)
            (2 0) (2 1) (2 2)
        (3 0) (3 1) (3 2) (3 3)
        (4 0) (4 1) (4 2) (4 3) (4 4)

Números combinatorios
(m n) + (m n + 1) = (m + 1 n + 1)

Esta es la manera de pasar de un caso a uno más sencillo. El número combinatorio con m+1 en la parte de arriba se calcula a partir de dos con m.
Casos obvios:
1. (m 0) = m! / 0!(m - 0)! = 1
2. (m m) = m! /m!(m - m)! = 1
3. (m 1) = m """


def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f - 1)


def combinatorio(m, n):
    if m < n:
        return "m debe ser mayor o igual a n."
    else:
        return factorial(m) // (factorial(n) * factorial(m - n))


def imprimir_triangulo_tartaglia(filas):
    for i in range(filas):
        for j in range(filas - i):
            print(" ", end=" ")
        for k in range(i + 1):
            print(combinatorio(i, k), end=" ")
        print()


m = 7
n = 5
f = 10
print(f"\nEl factorial de {f} es {factorial(f)}.\n")
print(f"({m} {n}) = {combinatorio(m, n)}.\n")
print("Triángulo de Tartaglia:")
imprimir_triangulo_tartaglia(5)
