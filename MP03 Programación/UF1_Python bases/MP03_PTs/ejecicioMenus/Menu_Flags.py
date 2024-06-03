# Inicializar las variables de los flags
menu_principal = True
opcion_1 = False
opcion_2 = False
opcion_3 = False

# Bucle principal del programa
while menu_principal:
    # Mostrar el menú principal
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")


    opcion = input("Selecciona una opción (1-4): ")

    # Verificar la opción ingresada
    if opcion == "1":
        opcion_1 = True
        opcion_2 = False
        opcion_3 = False
    elif opcion == "2":
        opcion_1 = False
        opcion_2 = True
        opcion_3 = False
    elif opcion == "3":
        opcion_1 = False
        opcion_2 = False
        opcion_3 = True
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        menu_principal = False
    else:
        print("Opción no válida. Por favor, ingresa una opción válida.")

    # Menú de la Opción 1
    while opcion_1:
        print("Estás en la Opción 1.")

        opcion_1 = False  # Regresar al menú principal

    # Menú de la Opción 2
    while opcion_2:
        print("Estás en la Opción 2.")

        opcion_2 = False  # Regresar al menú principal

    # Menú de la Opción 3
    while opcion_3:
        print("Estás en la Opción 3.")

        opcion_3 = False  # Regresar al menú principal
