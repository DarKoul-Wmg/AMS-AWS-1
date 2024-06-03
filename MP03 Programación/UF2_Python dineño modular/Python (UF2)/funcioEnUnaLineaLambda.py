"""EXPLICACIÓN:
Este código define una función formaLambda1 que toma un parámetro n y devuelve una función lambda que suma n al  que se
le pase. Luego, se invoca formaLambda1 dos veces con diferentes argumentos: 1 y 0. Esto crea dos funciones lambda
diferentes y las asigna a las variables f y g, respectivamente. Después, se realizan cuatro llamadas a estas funciones
lambda con diferentes argumentos:

- f(1): Se llama a la función f (que es una función lambda que suma 1) con el argumento 1, lo que resulta en 1 + 1 = 2.
- f(2): Se llama nuevamente a la función f con el argumento 2, resultando en 2 + 1 = 3.
- g(1): Se llama a la función g (que es una función lambda que suma 0) con el argumento 1, lo que resulta en 1 + 0 = 1.
- g(2): Se llama a la función g con el argumento 2, resultando en 2 + 0 = 2."""


def formaLambda1(n):
    return lambda x: x + n


f, g = formaLambda1(1), formaLambda1(0)
print(f(1))
print(f(2))
print(g(1))
print(g(2))
print("\n")

# ----------------------------------------------------------------------------------------------------------------------

"""EXPLICACIÓN:
Este código define una tupla llamada formaLambda2 que contiene dos funciones lambda:

- La primera función lambda toma dos argumentos x y n y devuelve la suma de ambos (x + n).
- La segunda función lambda también toma dos argumentos x y n, y devuelve la suma de ambos (x + n).
- Luego, el código realiza cuatro llamadas a estas funciones lambda utilizando los índices correspondientes en la tupla:

"Crida 1" llama a la segunda función lambda con los argumentos 1 y 1, resultando en 1 + 1 = 2.
"Crida 2" llama nuevamente a la segunda función lambda con los argumentos 2 y 1, resultando en 2 + 1 = 3.
"Crida 3" llama a la primera función lambda con los argumentos 1 y 0, resultando en 1 + 0 = 1.
"Crida 4" llama a la primera función lambda con los argumentos 2 y 1, resultando en 2 + 1 = 3."""

formaLambda2 = (lambda x, n: x + n, lambda x, n: x + n)

print("Crida 1:", formaLambda2[1](1, 1))
print("Crida 2:", formaLambda2[1](2, 1))
print("Crida 3:", formaLambda2[0](1, 0))
print("Crida 4:", formaLambda2[0](2, 1))
