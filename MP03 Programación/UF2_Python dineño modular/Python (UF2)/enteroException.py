def llegeix_sencer():
    """Sol·licita un valor sencer i el retorna.
    Si el valor teclejat no çes sencer, permet 4 intents per entrar correctament, de lo contrari, llança una
    excepció."""
    intents = 0
    while intents < 5:
        valor = input("Entra un número sencer.\n> ")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            intents += 1
            raise ValueError("Valor incorrecte. Has utilitzat cinc intents.")


print(llegeix_sencer())

# Versió 2:


def pedir_entero(max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        try:
            numero = int(input("Por favor, introduce un número entero.\n> "))
            return numero  # Devuelve el número entero si la conversión es exitosa
        except ValueError:
            print("Error: Debes introducir un número entero válido. Inténtalo de nuevo.")
            intentos += 1
            print(f"Te quedan {max_intentos - intentos} intentos.")
    raise ValueError("Se superó el número máximo de intentos.")

try:
    entero = pedir_entero()
    print("El número entero ingresado es:", entero)
except ValueError as e:
    print(e)  # Imprime el mensaje de error
except KeyboardInterrupt:
    print("\n¡Se ha interrumpido la ejecución del programa!")
