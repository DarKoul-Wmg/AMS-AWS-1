""" Exercici 1:
L'objectiu d'aquest exercici és dissenyar i implementar un programa que permeti analitzar mostres estadístiques. A tal
efecte seguirem els següents passos:
1. Dissenyeu i implementeu una funció que llegeixi del teclat una seqüència de reals i retorna la llista corresponent.
Assumiu que els valors són sempre positius o zero i que el primer negatiu que es llegeix actúa de sentinella.
2. Dissenyeu i implementeu una funció tal que donada una llista de reals de mida arbitraria en calcula la suma.
3. Dissenyeu i implementeu una funció tal que donada una llista de reals de mida arbitrària en calcula el màxim.
4. Dissenyeu i implementeu una funció tal que donada una llista de reals de mida arbitrària en calcula el mínim.
5. Dissenyeu i implementeu una funció tal que donada una llista de reals de mida arbitrària en calcula el recorregut.
6. Dissenyeu i implementeu una funció tal que donada una llista de reals de mida arbitrària en calcula la mitja.
7. Dissenyeu i implementeu una funció tal que donada una llista de reals de mida arbitrària en calcula la variància.

                                Fórmula:        V = i = n Σ i = 1 (Xi - X̄)2 / n - 1

A on:
- Xi són cadascun dels valors.
- X̄ és la mitja.
- n és la quantitat d’elements.

A continuació, escriviu un programa que presenti un menú a l'usuari i li permeti executar les següents opcions:
- Llegir dades: s’ha de verificar que continguin el valor correcte.
- Calcular el recorregut.
- Calcular la mitja.
- Calcular la variància.

Haureu construït el vostre propi calculador estadístic! """


# Función para leer una secuencia de números reales hasta que se introduce un número negativo
def leer_secuencia():
    secuencia = []
    while True:
        num = float(input("Introduce un número (introduce un número negativo para terminar): "))
        if num < 0:
            break
        secuencia.append(num)
    return secuencia


# Función para calcular la suma de una lista de números.
def calcular_suma(secuencia):
    return sum(secuencia)


# Función para calcular el máximo de una lista de números.
def calcular_maximo(secuencia):
    return max(secuencia)


# Función para calcular el mínimo de una lista de números.
def calcular_minimo(secuencia):
    return min(secuencia)


# Función para calcular el recorrido (rango) de una lista de números.
def calcular_recorrido(secuencia):
    return max(secuencia) - min(secuencia)


# Función para calcular la media (promedio) de una lista de números.
def calcular_media(secuencia):
    return sum(secuencia) / len(secuencia)


# Función para calcular la varianza de una lista de números.
def calcular_varianza(secuencia):
    media = calcular_media(secuencia)
    varianza = sum((x - media) ** 2 for x in secuencia) / (len(secuencia) - 1)
    return varianza


# Función principal que muestra un menú al usuario y realiza las operaciones seleccionadas.
def menu_estadistico():
    secuencia = []
    while True:
        print("\n\nMenú")
        print("1. Leer secuencia de números.")
        print("2. Calcular el recorrido.")
        print("3. Calcular la media.")
        print("4. Calcular la varianza.")
        print("5. Salir.")
        opcion = input("Selecciona una opción.\n> ")

        if opcion == "1":
            secuencia = leer_secuencia()
        elif opcion == "2":
            if secuencia:
                print("El recorrido es:", calcular_recorrido(secuencia))
            else:
                print("No se ha ingresado ninguna secuencia de números.")
        elif opcion == "3":
            if secuencia:
                print("La media es:", calcular_media(secuencia))
            else:
                print("No se ha ingresado ninguna secuencia de números.")
        elif opcion == "4":
            if secuencia:
                print("La varianza es:", calcular_varianza(secuencia))
            else:
                print("No se ha ingresado ninguna secuencia de números.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


# Ejecutar el programa principal
menu_estadistico()
