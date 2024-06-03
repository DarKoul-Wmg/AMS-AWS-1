# 5. Búsqueda binaria de manera recursiva.
"""La "búsqueda binaria" es un algoritmo de búsqueda utilizado para encontrar la posición de un valor objetivo dentro de
una lista ordenada. Este algoritmo divide repetidamente la lista en mitades y compara el valor objetivo con el elemento
en el medio de la lista. Si el valor objetivo es igual al elemento del medio, se devuelve la posición de ese elemento.
Si el valor objetivo es menor que el elemento del medio, la búsqueda se realiza en la mitad izquierda de la lista. Si el
valor objetivo es mayor que el elemento del medio, la búsqueda se realiza en la mitad derecha de la lista. Este proceso
se repite hasta que se encuentre el valor objetivo o hasta que no queden elementos por buscar.
La razón por la que se llama "búsqueda binaria" es porque divide repetidamente la lista en mitades, lo que resulta en
una búsqueda logarítmica, es decir, el tiempo de ejecución de la búsqueda aumenta de forma logarítmica con el tamaño de
la lista.
En el código, la función busqueda_binaria implementa la búsqueda binaria de manera recursiva. Toma una lista ordenada
(arr), un índice de inicio (inicio), un índice de fin (fin) y un valor objetivo (objetivo) como parámetros. La función
devuelve la posición del valor objetivo en la lista si se encuentra, o -1 si el valor objetivo no está presente en la
lista."""


def busqueda_binaria(arr, inicio, fin, objetivo):
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria(arr, medio + 1, fin, objetivo)
    else:
        return busqueda_binaria(arr, inicio, medio - 1, objetivo)


print("Búsqueda binaria:", busqueda_binaria([1, 2, 3, 4, 5], 0, 4, 3))