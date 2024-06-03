import os


def cambiar_nombre():
    while True:
        old = input("Extension a cambiar: ")
        new = input("Extension nueva: ")
        if old.isalpha() and len(old) == 3:
            if new.isalpha() and len(new) == 3:
                break
            else:
                print("Introduce un valor valido")
        else:
            print("Introduce un valor valido")
    directorio_actual = os.getcwd()
    archivos = os.listdir(directorio_actual)
    print(archivos)
    for element in archivos:
        if old in element:
            print(element)
            new_extension = element[:-3]
            new_extension += new
            os.rename(element,new_extension)

cambiar_nombre()
print(os.getcwd())
