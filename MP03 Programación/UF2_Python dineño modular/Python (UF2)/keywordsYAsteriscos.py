""" En Python, el uso de asteriscos (* y **) se utiliza para manejar parámetros variables en funciones.
Un solo asterisco (*) se emplea para recoger argumentos posicionales adicionales en una tupla.
Dos asteriscos (**) se utilizan para recoger argumentos de palabra clave adicionales en un diccionario."""


def suma_numeros(a, b, *args):
    suma = a + b
    for num in args:
        suma += num
    return suma


resultado = suma_numeros(1, 2, 3, 4, 5)
print("La suma es:", resultado)

# ----------------------------------------------------------------------------------------------------------------------
print("\n")


def imprimir_datos(nombre, edad, **kwargs):
    print("Nombre:", nombre)
    print("Edad:", edad)
    for clave, valor in kwargs.items():
        print(clave.capitalize() + ":", valor)


imprimir_datos("Juan", 30, ciudad="Madrid", profesion="Ingeniero")

# ----------------------------------------------------------------------------------------------------------------------
print("\n")


def saludar(nombre, saludo="Hola", emoticon="😊"):
    print(f"{saludo}, {nombre} {emoticon}")


saludar("Ana", saludo="¡Hola", emoticon="😄")

# ----------------------------------------------------------------------------------------------------------------------
print("\n")


def detalles_persona1(nombre, **detalles):
    print(f"Nombre: {nombre}")
    for clave, valor in detalles.items():
        print(f"{clave}: {valor}")


info_persona = {"edad": 25, "ciudad": "Barcelona", "profesion": "Doctor"}
detalles_persona1("Ana", **info_persona)

# ----------------------------------------------------------------------------------------------------------------------
print("\n")


def detalles_persona2(nombre, edad=0, **otros_detalles):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    for clave, valor in otros_detalles.items():
        print(f"{clave}: {valor}")


detalles_persona2("Elena", edad=35, ciudad="Valencia", profesion="Abogado")

