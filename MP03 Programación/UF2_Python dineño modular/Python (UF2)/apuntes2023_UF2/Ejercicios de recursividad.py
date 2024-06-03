import random


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 1. Dada una frase y una letra, devolver la frase desde la letra hasta el final.
def desde_letra_al_final(frase, letra):
    indice = frase.find(letra)
    if indice == -1:
        return "La letra no se encuentra en la frase."
    else:
        return frase[indice:]


frase = "Esta es una frase de ejemplo."
letra = "e"
print("Desde la letra al final:", desde_letra_al_final(frase, letra))
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 2. Dada una frase y una letra, devolver la frase desde el principio hasta la letra.
def desde_el_principio_hasta_letra(frase2, letra2):
    indice = frase.find(letra)
    if indice == -1:
        return "La letra no se encuentra en la frase."
    else:
        return frase[:indice + 1]


frase2 = "Esta es una frase de ejemplo"
letra2 = "e"
print("Desde el principio hasta la letra:", desde_el_principio_hasta_letra(frase, letra))
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 3. Dada una frase devolver la frase al revés.
def fraseAlReves(frase):
    if len(frase) == 1 or frase == "":
        return frase
    else:
        return frase[len(frase) - 1] + fraseAlReves(frase[1:len(frase) - 1]) + frase[0]


print(fraseAlReves("Claudia se va de vacaciones porque no aguanta más."))
print("\n" + "—" * 60 + "\n")
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# —————————————————————————————————————————————— PRÀCTICA 1: RECURSIVITAT ——————————————————————————————————————————————
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 1) Programar un algoritme recursiu que permeti fer la divisió per restes successives.
def division_resta(numerador, denominador):
    if numerador < denominador:
        return 0, numerador
    else:
        cociente, resto = division_resta(numerador - denominador, denominador)
        return cociente + 1, resto


numerador = int(input("Ingrese el numerador: "))
denominador = int(input("Ingrese el denominador: "))
cociente, resto = division_resta(numerador, denominador)
print("Cociente:", cociente)
print("Resto:", resto)
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 2). Programar un algoritme recursiu que permeti sumar els dígits d’un número.
def sumar_digitos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + sumar_digitos(numero // 10)


numero = int(input("Ingrese un número.\n> "))
print("La suma de los dígitos es:", sumar_digitos(numero))
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 3). Programar un algoritme recursiu que permeti sumar els elements d’una llista.
def sumarelements(lista, comodin=0):
    # También se puede poner if lista == [], pero Python lo prefiere así.
    if not lista:
        return comodin
    else:
        n = lista[0]
        return n + sumarelements(lista[1:], comodin)


def sumarelements2(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sumarelements2(l[1:])


lista = [20, 11, 2021]
print("Suma de los elementos de la lista usando sumarelements:", sumarelements(lista))
print("Suma de los elementos de la lista usando sumarelements2:", sumarelements2(lista))
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 4). Escriure la funció Potencia(x, y) = x^y de manera recursiva.
def potencia(x, y):  # P.E. 4 ^ 3
    if y == 1:
        return x
    else:
        return x * potencia(x, y - 1)  # P.E. 4 * 4 ^ 2


base = int(input("Base:\n> "))
exponente = int(input("Exponente:\n> "))
print(f"{base} elevado a {exponente} es igual a {potencia(base,exponente)}.")
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 5. Escriure el producte de dos números de manera recursiva. Ajuda: 2x3 implica sumar tres vegades el número dos.
def producto_recursivo(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + producto_recursivo(a, b - 1)


num1 = int(input("Ingrese el primer número.\n> "))
num2 = int(input("Ingrese el segundo número.\n> "))

resultado = producto_recursivo(num1, num2)
print("El producto de", num1, "y", num2, "es:", resultado)
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 6. Programar una funció recursiva que permeti multiplicar els elements d’un Array.
def multiplicar_elementos(lista):
    if len(lista) == 0:
        return 1
    else:
        return lista[0] * multiplicar_elementos(lista[1:])


lista_numeros = [2, 3, 4, 5]
print("El producto de los elementos de la lista es:", multiplicar_elementos(lista_numeros))
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 7. Escriure un programa que trobi la suma dels enters positius parells des de N fins a 2.
def suma_pares_positivos(n):
    if n <= 2:
        return 0
    elif n % 2 != 0:
        # Si n es impar, lo decrementamos para hacerlo par.
        n -= 1
    return n + suma_pares_positivos(n - 2)


numero = int(input("Ingrese un número entero positivo.\n> "))
resultado = suma_pares_positivos(numero)
print("La suma de los enteros positivos pares desde", numero, "hasta 2 es:", resultado)
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 8. Escriure una funció recursiva que imprimeixi per pantalla els valors des d'1 fins a un número introduït per
# l'usuari.
def imprimir_hasta_n(numero):
    if numero == 1:
        print(numero)
    else:
        imprimir_hasta_n(numero - 1)
        print(numero)


n = int(input("Introduce un número entero positivo.\n> "))
if n > 0:
    imprimir_hasta_n(n)
else:
    print("Por favor, introduce un número entero positivo.")
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 9. Dissenyeu una funció recursiva tal que, donat dos vectors de número sencers,
# retorni un booleà indicant si són iguals, és a dir, si tenen els mateixos valors a
# les mateixes posicions.
def dosvectors(v1, v2):
    # Longitud diferente --> vectores diferentes.
    if len(v1) != len(v2):
        return False

    # Al encontrar un componente diferente, los vectores son diferentes.
    elif v1[0] != v2[0]:
        return False

    # Aquí sabemos que la primera componente es igual.
    # Hemos llegado al final y no hemos visto ninguna diferencia.
    elif len(v1) == 1:
        return True
    # Aún no estamos seguros. Hay que inspeccionar el resto de los vectores.
    else:
        return dosvectors(v1[1:], v2[1:])


v1 = [1, 2, 3, 4, 5, 6]
v2 = [1, 2, 3, 4, 5]
v3 = [1, 2, 0, 4, 5, 6]
v4 = [1, 2, 3, 4, 5, 6]

print(f"{v1} es igual a {v2}. {dosvectors(v1, v2)}")
print(f"{v1} es igual a {v3}. {dosvectors(v1, v3)}")
print(f"{v1} es igual a {v4}. {dosvectors(v1, v4)}")
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 10. Donat un vector de nombres enters ordenat decreixentment, dissenyeu un programa
# recursiu que comprovi si el valor d’algun dels elements del vector coincideix amb el seu
# índex.
def coincide_con_indice(vector, inicio=0):
    if len(vector) == 0:
        return False
    elif vector[0] == inicio:
        return True
    else:
        return coincide_con_indice(vector[1:], inicio + 1)


vector1 = [5, 4, 3, 2, 1]
vector2 = [10, 8, 6, 4, 2, 0]

print("¿Alguno de los elementos coincide con su índice en el primer vector?", coincide_con_indice(vector1))
print("¿Alguno de los elementos coincide con su índice en el segundo vector?", coincide_con_indice(vector2))
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 11. Programa recursiu que demani a l’usuari una frase i la repeteixi un determinat número de vegades.
def repetir_frase(frase, veces):
    if veces == 0:
        return ""
    else:
        return frase + "\n" + repetir_frase(frase, veces - 1)


frase_usuario = input("Ingresa una frase: ")
num_veces = int(input("Ingresa el número de veces que deseas repetir la frase: "))
print(repetir_frase(frase_usuario, num_veces))
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 13. Programa recursiu que comprovi si un número està en un rang de valors.
def esta_en_rango(numero, rango_inicio, rango_fin):
    if numero == rango_inicio or numero == rango_fin:
        return True
    elif numero < rango_inicio or numero > rango_fin:
        return False
    else:
        return esta_en_rango(numero, rango_inicio + 1, rango_fin - 1)


numero = int(input("Ingrese un número.\n> "))
inicio = int(input("Ingrese el inicio del rango.\n> "))
fin = int(input("Ingrese el final del rango.\n> "))

if esta_en_rango(numero, inicio, fin):
    print(f"El número {numero} está en el rango [{inicio}, {fin}].")
else:
    print(f"El número {numero} NO está en el rango [{inicio}, {fin}].")
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 14. Escriure un programa recursiu que insereixi valors aleatoris en una llista.
def insertaAleatorios(lista, n):
    if len(lista) == n:
        return lista
    else:
        num = random.randint(1, 10)
        lista.append(num)
        return insertaAleatorios(lista, n)


lista = []
n = int(input("Dime cuántos números quieres que haya en la lista:\n> "))
print(insertaAleatorios(lista, n))
print("\n" + "—" * 60 + "\n")


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 15. Escriure un programa recursiu que insereixi valors sense que es repeteixin.
def insertaAleatorios(lista, n):
    if len(lista) == n:
        return lista
    else:
        num = random.randint(1, 10)
        while num in lista:
            num = random.randint(1, 10)
        lista.append(num)
        return insertaAleatorios(lista, n)


lista = []
n = int(input("Dime cuántos números quieres que haya en la lista.\n> "))
print(insertaAleatorios(lista, n))
print("\n" + "—" * 60)
