def repetir_frase(frase, n):
    if n == 0:
        return
    else:
        print(frase)
        return repetir_frase(frase, n - 1)


frase = input("Introduce una frase: ")
repeticiones = int(input("Introduce el número de repeticiones: "))
print("Repetición de la frase:")
repetir_frase(frase, repeticiones)
