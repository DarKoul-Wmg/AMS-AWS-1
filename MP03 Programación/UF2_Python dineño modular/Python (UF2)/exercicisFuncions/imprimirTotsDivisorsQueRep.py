# Ejercicio 3
"""3. Escriure el codi de la funció que imprimeixi per pantalla tots els divisors del número que rep com argument."""


def imprimir_divisores(numero):
    print("Divisores de", numero, end="" + ":\n")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)


imprimir_divisores(10)
print("\n")
imprimir_divisores(20)
print("\n")
imprimir_divisores(30)
