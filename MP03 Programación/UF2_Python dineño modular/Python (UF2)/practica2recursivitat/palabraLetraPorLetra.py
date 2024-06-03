def mostrar_subpalabras(palabra):
    if not palabra:
        return
    else:
        print(palabra)
        mostrar_subpalabras(palabra[:-1])


palabra = "Benvinguts a tots"
print("Subpalabras de la palabra:")
mostrar_subpalabras(palabra)

def mostrar_subpalabras(palabra):
    for i in range(len(palabra)):
        print(palabra[:i+1])

palabra = "Benvinguts"
print("Subpalabras de la palabra:")
mostrar_subpalabras(palabra)
