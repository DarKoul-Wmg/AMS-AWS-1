def llegeix0a10():
    num = int(input("Introduce un numero entre 0-10: "))
    while not num in range(0,11):
        num = int(input("Numero no valido, tiene que ser entre 0-10: "))
    else:
        print("Número válido")



llegeix0a10()