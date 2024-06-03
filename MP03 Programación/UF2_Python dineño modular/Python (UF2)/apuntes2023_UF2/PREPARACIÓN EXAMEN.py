""" RECURSIÓ                                               Clàudia Moyano Herrerias (1r DAW)"""
from colorama import Fore, Back
# —————————————————————————————————————————————————————————————————————————————————————————————
# —————————————————————————————— 1. RECURSIVIDAD DE CONTAR ATRÁS ——————————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.LIGHTMAGENTA_EX, Back.LIGHTWHITE_EX + "1. RECURSIVIDAD DE CONTAR ATRÁS." + Back.RESET)
print(Fore.LIGHTWHITE_EX)


def cuentatras(n):
    if n < 0:
        print("¡Fin!")
        # Acaba aquí, ya que ha llegado a 0.
    else:
        print(n)
        cuentatras(n - 1)
        # Restar el número. Con el "if" realizado comprueba el número hasta que es menor que 0.


cuentatras(10)
print("\n")

# —————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————— 2. RECURSIVIDAD DE CONTAR ADELANTE ————————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.LIGHTCYAN_EX, Back.LIGHTWHITE_EX + "2. RECURSIVIDAD DE CONTAR ADELANTE." + Back.RESET)
print(Fore.LIGHTWHITE_EX)


def cuentadelante(m, n):
    if m == n:
        print("Hemos encontrado el caso base", m)
        # ¡Ya ha llegado a donde debe contar! :)
    else:
        print("No hemos encontrado el caso base", m)
        cuentadelante(m + 1, n)
        # Añadimos un número consecutivamente a "m" hasta que llegue a ser igual que "n".
        print("Estamos saliendo de la recursión", m)
        # Salimos de la recursión (es opcional escribir esto).


cuentadelante(10, 15)
print("\n")

# —————————————————————————————————————————————————————————————————————————————————————————————
# —————————————————————————————— 3. RECURSIVIDAD DE UN FACTORIAL ——————————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.LIGHTGREEN_EX, Back.LIGHTWHITE_EX + "3. RECURSIVIDAD DE UN FACTORIAL." + Back.RESET)
print(Fore.LIGHTWHITE_EX)


def fact(n):
    if n == 0:
        resultado = 1
        print("Hemos llegado al caso base", n)
    else:
        print("No hemos llegado al caso base", n)
        f = fact(n - 1)
        resultado = n * f
        # Multiplicamos el número con el factorial realizado antes.
        print("Estamos saliendo de la recursión", n, f, resultado)
        # Salimos de la recursión (es opcional escribir esto).
    return resultado


print(fact(5))
print("\n")

# —————————————————————————————————————————————————————————————————————————————————————————————
# ——————————————————————————————— 4. RECURSIVIDAD DE UNA POTENCIA —————————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.LIGHTRED_EX, Back.LIGHTWHITE_EX + "4. RECURSIVIDAD DE UNA POTENCIA." + Back.RESET)
print(Fore.LIGHTWHITE_EX)


def potencia(base, exp):
    if exp == 0:
        resultado = 1
        print("Hemos encontrado el caso base", exp)
    else:
        print("No hemos alcanzado el caso base", exp)
        potencia_anterior = potencia(base, exp - 1)
        # Realizamos la fórmula.
        resultado = base * potencia_anterior
        # Obtenemos el resultado al multiplicar la base con la fórmula realizada anteriormente.
        print("Estamos saliendo de la recursión", base, potencia_anterior, resultado)
        # Salimos de la recursión (es opcional escribir esto).
    return resultado


print(potencia(2, 4))


# SEGUNDA VERSIÓN. ————————————————————————————————————————————————————————————————————————————
def potencia1(base1, exp1):
    if exp1 == 0:
        return 1
    # Hay que recordar que si el exponente es 0, siempre da 1.
    else:
        return base1 * potencia1(base1, exp1 - 1)
        # Devolvemos automáticamente el resultado de la operación de la potencia.


print(potencia1(2, 4))
print("\n")

# —————————————————————————————————————————————————————————————————————————————————————————————
# ——————————————————————————————— 5. SUMAR ELEMENTOS DE UNA LISTA —————————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.LIGHTBLUE_EX, Back.LIGHTWHITE_EX + "5. SUMAR ELEMENTOS DE UNA LISTA." + Back.RESET)
print(Fore.LIGHTWHITE_EX)
lista = [1, 2, 3, 4, 5, 6, 7]


def sumar(lista):
    if not lista:  # También: if lista == []:
        return 0
    # No hay lista. ¿Para qué hacer algo?
    else:
        return lista[0] + sumar(lista[1:])
        # Con "lista[0]" se refiere al primer elemento de la lista.
        # Con "(lista[1:]" se refiere al primer elemento hasta el último de la lista.


print(sumar(lista))
print("\n")

# —————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————— 6. INVERTIR UNA LISTA DE FORMA RECURSIVA ——————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.BLACK, Back.LIGHTWHITE_EX + "6. INVERTIR UNA LISTA DE FORMA RECURSIVA." + Back.RESET)
print(Fore.LIGHTWHITE_EX)
lista1 = [1, 2, 3, 4, 5]


def invertirlista(lista1):
    if not lista1:  # También: if lista1 == []:
        return lista1
        # Se devuelve la lista vacía.
    else:
        return [lista1[-1]] + invertirlista(lista1[:-1])
        # Con [lista1[-1]] se refiere al último elemento.
        # Con (lista[:-1] se refiere a todos menos el último incluido.


print(invertirlista(lista1))
print("\n")


# —————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————— 12. CREAR LISTA DE NÚMEROS PARES RECURSIVAMENTE ———————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.LIGHTBLACK_EX, Back.LIGHTWHITE_EX + "12. CREAR LISTA DE NÚMEROS PARES RECURSIVAMENTE." + Back.RESET)
print(Fore.LIGHTWHITE_EX)


def listapares(n, m):
    if n > m:
        return []
    # Tiene que ir de "n" a "m" (siendo "m" más grande).
    elif n % 2 == 0:
    # Operación para conseguir los números pares.
        return [n] + listapares(n + 1, m)
        # Devuelve el número escogido (10), sumándole uno hasta llegar a "m".
    else:
        return listapares(n + 1, m)
        # Devuelve el número escogido (10), sumándole uno hasta llegar a "m".


print(listapares(10, 20))
print("\n")

# —————————————————————————————————————————————————————————————————————————————————————————————
# ———————————————————————— 13. SUMAR LOS ELEMENTOS PARES DE UNA LISTA —————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.RED, Back.LIGHTWHITE_EX + "13. SUMAR LOS ELEMENTOS PARES DE UNA LISTA." + Back.RESET)
print(Fore.LIGHTWHITE_EX)
unalista = [3, 4, 8, 9, 12, 15, 24]


def sumarpares(lista2, i=0, suma=0):
    if len(lista2) == i:
        return suma
        # En el índice ("i") hay un 0.
    elif lista2[i] % 2 == 0:
    # Operación para conseguir los números pares.
        suma += lista2[i]
        return sumarpares(lista2, i + 1, suma)
        # Con "i + 1" se refiere a empezar desde el segundo elemento de la lista (4).


print(sumarpares(unalista))
print("\n")

# —————————————————————————————————————————————————————————————————————————————————————————————
# ———————————————————— 14. RESTAR ELEMENTOS DE UNA LISTA DE FORMA RECURSIVA ———————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.BLUE, Back.LIGHTWHITE_EX + "14. RESTAR ELEMENTOS DE UNA LISTA DE FORMA RECURSIVA." + Back.RESET)
print(Fore.LIGHTWHITE_EX)
lista3 = [2, 3, 4, 5]


def restar(lista3):
    if len(lista3) == 0:
        return 0
    else:
        return restar(lista3[:-1]) - lista3[-1]


print(restar(lista3))
print("\n")


# —————————————————————————————————————————————————————————————————————————————————————————————
# ———————————————————————— 15. CONVERTIR NÚMERO DECIMAL A NÚMERO OCTAL ————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
print("\n" + Fore.MAGENTA, Back.LIGHTWHITE_EX + "16. EXERCICI LUIS" + Back.RESET)
print(Fore.LIGHTWHITE_EX)


def convertirenterobase(numero, base):
    conversioncadena = "0123456789ABCDEF"
    # Variable. De 0 hasta 15, sabiendo que la base máxima es 16 (hexadecimal).
    if numero < base:
    # Si es así...
        return conversioncadena[numero]
        # ... devolvemos lo que hay en cadena, en posición número.
    else:
        return convertirenterobase(numero//base, base) + conversioncadena[numero % base]
        # Devolvemos la división de número entre base y base (que será siempre la misma): Le
        # concatenamos lo que hay en "conversioncadena" y calculamos el módulo de número entre base.


numero = 230
base = 16
resultado = convertirenterobase(numero, base)
print(resultado)
print("\n")

# —————————————————————————————————————————————————————————————————————————————————————————————
# ———————————————————————— 16. EXERCICI ORDENAR DICCIONARIS AMB FUNCIÓ ————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————
# Funció que rep un paràmetre fix que pot ser "ASC" o "DESC", un nombre variable de parells
# nom_alumne=nota. Retorna una llista amb els alumnes ordenats "ASC" o "DESC" segons la nota.
# Si el primer paràmetre és incorrecte, excepte ValueError. Si no rep almenys un alumne-nota,
# genera excepció ValueError.
print("\n" + Fore.YELLOW, Back.LIGHTWHITE_EX + "16. EXERCICI LUIS" + Back.RESET)
print(Fore.LIGHTWHITE_EX)
while True:
    orden = input("¿Deseas ordenar de forma ascendente (ASC) o descendente (DESC)?\n> ").upper()
    posibles = ["ASC", "DESC"]
    try:
        if orden in posibles:
            break
        else:
            raise ValueError
    except ValueError:
        print("¡Orden no válido! Solo puedes escribir \"ASC\" o \"DESC\".")


def funcion(orden, **kwords):
    lista = []
    keys = list(kwords.keys())
    if orden == "ASC":
        for pasadas in range(len(kwords)):
            for comp in range(len(kwords)-pasadas-1):
                if kwords[keys[comp]] > kwords[keys[comp+1]]:
                    keys[comp], keys[comp+1] = keys[comp+1], keys[comp]
    if orden == "DESC":
        for pasadas in range(len(kwords)):
            for comp in range(len(kwords)-pasadas-1):
                if kwords[keys[comp]] < kwords[keys[comp+1]]:
                    keys[comp], keys[comp+1] = keys[comp+1], keys[comp]
    for i in keys:
        print(i, kwords[i])


funcion(orden, Claudia=6, Diego=9, Maribel=10, Laura=1)
