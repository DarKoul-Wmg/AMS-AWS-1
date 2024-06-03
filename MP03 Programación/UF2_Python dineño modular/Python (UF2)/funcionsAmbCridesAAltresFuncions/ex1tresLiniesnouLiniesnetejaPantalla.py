"""Exercici 1:
Crea un programa que contingui les següents funcions:
- Funció tres_linies per a mostrar tres línies en blanc.
- Funció nou_linies que utilitzi la funció tres_linies per a mostrar nou línies en blanc.
- Funció neteja_pantalla que mostri vint-i-cinc línies en blanc.
- L'última instrucció del fitxer ha de ser una crida a neteja_pantalla.
- Mou la crida a la funció neteja_pantalla a l’inici del programa. Executa el programa i explica què succeeix.
- Crea la funció de concatena_n_vegades que mostri la cadena c, n vegades. El prototipus de la funció és el següent:
    def concantena_n_vegades(c, n):
        'Crea el teu codi'"""


def tres_linies():
    print("\n" * 3)


def nou_linies():
    tres_linies()
    tres_linies()
    tres_linies()


def neteja_pantalla():
    print("\n" * 25)


def concatena_n_vegades(c, n):
    for _ in range(n):
        print(c, end='')


neteja_pantalla()
tres_linies()
nou_linies()
concatena_n_vegades("Hola ", 3)
