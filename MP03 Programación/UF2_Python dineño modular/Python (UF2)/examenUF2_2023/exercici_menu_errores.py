def exercici1(options, exceptions=("A",)):
    # Comprovació de tipus i longitud mínima.
    if not isinstance(options, tuple):
        raise ValueError("The options have to be a tuple.")
    if not isinstance(exceptions, tuple):
        raise ValueError("The exceptions have to be a tuple.")
    if len(options) < 2:
        raise ValueError("The minimum length of the options is 2.")

    while True:
        # Mostra el menú.
        print("\n".join(f"{i + 1}) {option}" for i, option in enumerate(options)))
        try:
            # Llegir l'opció de l'usuari.
            user_input = input("Option.\n> ")

            # Comprovació si l'opció és un nombre.
            if not user_input.isdigit():
                if user_input in exceptions:
                    return user_input
                else:
                    raise ValueError("The option is not a number and is not in exceptions.")

            # Converteix l'entrada a un número sencer
            choice = int(user_input)

            # Comprovació si l'opció és dins del rang vàlid
            if 1 <= choice <= len(options):
                return choice
            elif user_input in exceptions:
                return user_input
            else:
                raise ValueError("The option is out of range and not in exceptions.")
        except ValueError as e:
            print(f"Error: {e}")
            input("Enter to continue")


# Exemple d'ús
tupla = ("opcio1", "opcio2", "opcio3")
result = exercici1(tupla, exceptions=("c", "d", 10, "11"))
print(result)
