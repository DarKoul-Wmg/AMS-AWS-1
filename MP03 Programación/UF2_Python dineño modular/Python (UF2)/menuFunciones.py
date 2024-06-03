# Función para crear un nuevo usuario.
def crear_usuario(usuarios):
    print("\nCreación de un nuevo usuario.")
    nombre = input("Nombre.\n> ")
    apellido = input("Apellido.\n> ")
    dni = input("DNI.\n> ")
    telefono = input("Teléfono.\n> ")

    # Verificar si el DNI o el teléfono ya existen en la lista de usuarios.
    for usuario in usuarios:
        if usuario["DNI"] == dni:
            print("Error: Este DNI ya está registrado.")
            return
        if usuario["Teléfono"] == telefono:
            print("Error: Este teléfono ya está registrado.")
            return

    # Si no se encontraron coincidencias, agregar el nuevo usuario a la lista
    usuario = {"Nombre": nombre, "Apellido": apellido, "DNI": dni, "Teléfono": telefono}
    usuarios.append(usuario)
    print("Usuario creado exitosamente.")


def calcular_letra_dni(numero_dni):
    tabla_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    resto = int(numero_dni) % 23
    letra = tabla_letras[resto]
    return letra


# Modificamos la función validar_dni para utilizar la nueva lógica.
def validar_dni(dni):
    # Comprobar que el DNI tiene longitud 9 y los primeros 8 caracteres son dígitos.
    if len(dni) != 9 or not dni[:8].isdigit():
        return False

    # Calcular la letra del NIF.
    letra_calculada = calcular_letra_dni(dni[:8])

    # Comprobar que la letra calculada coincide con la letra proporcionada en el DNI.
    if letra_calculada == dni[8].upper():
        return True
    else:
        return False


# Función para validar el formato del teléfono.
def validar_telefono(telefono):
    # Comprobar que el teléfono tiene longitud 9 y todos los caracteres son dígitos.
    return len(telefono) == 9 and telefono.isdigit()


# Función para listar usuarios por nombre.
def listar_por_nombre(usuarios):
    print("\nListado de usuarios por nombre")
    ordenar_burbuja(usuarios, "Nombre")
    imprimir_tabla_usuarios(usuarios)


# Función para listar usuarios por apellido
def listar_por_apellido(usuarios):
    print("\nListado de usuarios por apellido")
    ordenar_burbuja(usuarios, "Apellido")
    imprimir_tabla_usuarios(usuarios)


# Función para listar usuarios por DNI.
def listar_por_dni(usuarios):
    print("\nListado de usuarios por DNI")
    ordenar_burbuja(usuarios, "DNI")
    imprimir_tabla_usuarios(usuarios)


# Función para listar usuarios por teléfono.
def listar_por_telefono(usuarios):
    print("\nListado de usuarios por teléfono")
    ordenar_burbuja(usuarios, "Teléfono")
    imprimir_tabla_usuarios(usuarios)


# Función para imprimir los usuarios en formato de tabla.
def imprimir_tabla_usuarios(usuarios):
    print("{:<15} {:<15} {:<10} {:<15}".format("NOMBRE", "APELLIDO", "DNI", "TELÉFONO"))
    print("*" * 50)
    for usuario in usuarios:
        print("{:<15} {:<15} {:<10} {:<15}".format(usuario["Nombre"], usuario["Apellido"], usuario["DNI"],
                                                   usuario["Teléfono"]))


# Función de ordenación burbuja.
def ordenar_burbuja(usuarios, clave):
    n = len(usuarios)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if usuarios[j][clave] > usuarios[j + 1][clave]:
                usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]


# Función principal que ejecuta el menú.
def menu():
    usuarios = []
    while True:
        print("\nMenu:")
        print("1. Crear usuario.")
        print("2. Listar usuarios.")
        print("3. Salir.")

        opcion = input("Selecciona una opción.\n> ")

        if opcion == "1":
            crear_usuario(usuarios)
        elif opcion == "2":
            while True:
                print("\nListar usuarios por:")
                print("1. Nombre.")
                print("2. Apellido.")
                print("3. DNI.")
                print("4. Teléfono.")
                print("5. Volver al menú principal.")

                opcion_listar = input("Selecciona una opción: ")

                if opcion_listar == "1":
                    listar_por_nombre(usuarios)
                elif opcion_listar == "2":
                    listar_por_apellido(usuarios)
                elif opcion_listar == "3":
                    listar_por_dni(usuarios)
                elif opcion_listar == "4":
                    listar_por_telefono(usuarios)
                elif opcion_listar == "5":
                    break
                else:
                    print("Opción no válida. Por favor, selecciona una opción válida.")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


menu()
