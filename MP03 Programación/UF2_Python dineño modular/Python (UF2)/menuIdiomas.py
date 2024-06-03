def mostrar_menu():
    while True:
        idioma = input("¿Qué idioma prefieres? (0 - Catalán, 1 - Castellano): ")

        if idioma == '0':
            menu_catalan()
            break
        elif idioma == '1':
            menu_castellano()
            break
        else:
            print("Opción no válida. Por favor, selecciona 0 o 1.\n")


def menu_catalan():
    print("\nBenvingut al menú:")
    print("1. Opció 1.")
    print("2. Opció 2.")
    print("3. Opció 3.")


def menu_castellano():
    print("\nBienvenido al menú:")
    print("1. Opción 1.")
    print("2. Opción 2.")
    print("3. Opción 3.")


mostrar_menu()
