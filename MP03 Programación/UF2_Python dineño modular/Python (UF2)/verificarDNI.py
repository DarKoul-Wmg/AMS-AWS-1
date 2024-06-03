def calcular_letra_dni(numero_dni):
    tabla_letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    resto = int(numero_dni) % 23
    letra = tabla_letras[resto]
    return letra


def comprobar_dni(dni_completo):
    if len(dni_completo) != 9:
        return False

    numero_dni = dni_completo[:8]
    letra_dni = dni_completo[8].upper()

    letra_calculada = calcular_letra_dni(numero_dni)

    return letra_calculada == letra_dni


# Ejemplo de uso:
dni = "44121175e"
if comprobar_dni(dni):
    print(f"El DNI {dni} es válido.")
else:
    print(f"El DNI {dni} no es válido.")


# Para un ejercicio:
def calcular_letra_dni2(numero_dni):
    tabla_letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    resto = int(numero_dni) % 23
    letra = tabla_letras[resto]
    return letra


def comprobar_dni2(dni_completo):
    if len(dni_completo) != 9:
        return False

    numero_dni = dni_completo[:8]
    letra_dni = dni_completo[8].upper()

    letra_calculada = calcular_letra_dni(numero_dni)

    return letra_calculada == letra_dni


# Solicitar al usuario su DNI para comprobarlo
print("\n")
dni = input("Por favor, ingrese su DNI.\n> ")

if comprobar_dni2(dni):
    print(f"El DNI {dni} es válido.")
else:
    print(f"El DNI {dni} no es válido.")
