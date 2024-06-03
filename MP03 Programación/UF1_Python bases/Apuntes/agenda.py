cabezera = 'Agenda'.center(40,'*') + '\n' + 'Nombre'.ljust(20) + 'Telefono'.rjust(10)+ '\n' + '*'*40 + '\n'
datos=''
añadir = ''
while True:
    print("\n--- Agenda Simple ---")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Salir")
    print()
    opcion = input("Seleccione una opción 1 al 3 >  ")
    print()
    
    if opcion == "1":
        print(cabezera)
        nombre = input('Dime el nuevo nombre  > ')
        numero = input('Dime el nuevo telefono > ')
        añadir = input('Quieres añadir este numero a la agenda S \ N > ')
        if añadir=='S':
            datos = datos + nombre.ljust(20) + numero.rjust(10)+ '\n'
        else:
            print('No se ha añadido')                 

    elif opcion == "2":
        input('Press to continue')
        print(cabezera)
        print(datos)
        input('Press to continue')
       
    elif opcion == "3":      
        print("Gracias por usar la agenda. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3).")