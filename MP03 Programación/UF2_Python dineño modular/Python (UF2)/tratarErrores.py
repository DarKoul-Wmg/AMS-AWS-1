def division():
    try:
        numerador = int(input("Ingrese el numerador.\n> "))
        denominador = int(input("\nIngrese el denominador.\n> "))
        resultado = numerador / denominador
        print("El resultado de la división es:", resultado)
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except Exception as e:
        print("Error:", e)

try:
    division()
except KeyboardInterrupt:
    print("\nOperación interrumpida por el usuario.")
finally:
    print("\nPrograma finalizado.")


# Recursivo:
def division():
    try:
        numerador = int(input("Ingrese el numerador.\n> "))
        denominador = int(input("\nIngrese el denominador.\n> "))
        if denominador == 0:
            print("Error: No se puede dividir por cero.")
            # Llamada recursiva para que el usuario ingrese un nuevo denominador
            division()
        else:
            resultado = numerador / denominador
            print("El resultado de la división es:", resultado)
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")
        # Llamada recursiva para volver a intentar la división
        division()
    except Exception as e:
        print("Error:", e)

try:
    division()
except KeyboardInterrupt:
    print("\nOperación interrumpida por el usuario.")
finally:
    print("\nPrograma finalizado.")
