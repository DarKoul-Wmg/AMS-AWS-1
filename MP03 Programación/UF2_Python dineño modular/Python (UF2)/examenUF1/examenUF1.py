import random

# Listas proporcionadas
name_list = ["Mario Torres Cuesta", "Patricia Robles Fonseca", "Miranda Lopez Castaño", "Pablo Aguirre Santacana", "Laura Trimiño Serra", "Esteban Flores Jimenez"]
code_list = ["634SUV-76", "939CFO-44", "274MAR-43", "389JHL36", "993PRZ 12", "834ASD-86", "783JHM-54", "945GZT-75"]
game_list = ["Tennis", "Ping-Pong", "Indoor Football", "Chess", "Basketball", "Swimming"]

# Diccionario para almacenar los datos de los estudiantes
summer_camp_students = {}

while True:
    # Menú principal
    print("***Welcome to the Casal WeWantLearnProgramming****\n")
    print("1) Init Data")
    print("2) Find Users")
    print("3) List Users")
    print("4) Exit")

    # Solicitar opción al usuario
    option = input("Option: ")

    # Procesar la opción seleccionada
    if option == "1":
        # Generar 5 alumnos aleatorios
        for _ in range(5):
            # Elegir aleatoriamente un código que no esté en el diccionario
            code = random.choice(code_list)
            while code in summer_camp_students:
                code = random.choice(code_list)

            # Elegir aleatoriamente un nombre que no esté en el diccionario
            name = random.choice(name_list)
            while name in [student_data['name'] for student_data in summer_camp_students.values()]:
                name = random.choice(name_list)

            # Generar datos aleatorios
            dni = ''.join(random.choice('0123456789') for _ in range(8)) + random.choice('TRWAGMYFPDXBNJZSQVHLCKE')
            antiquity = random.randint(0, 10)
            num_games = random.randint(1, len(game_list))
            games = random.sample(game_list, num_games)

            # Añadir al diccionario
            summer_camp_students[code] = {'dni': dni, 'name': name, 'antiquity': antiquity, 'games': games}

        print("Initialization complete. 5 students added to the dictionary.")

    elif option == "2":
        print("Finding users...\n")

        # Solicitar criterio de búsqueda al usuario
        search_criteria = input("Enter search criteria (name, dni, or games): ").lower()

        # Iniciar tabla para mostrar resultados
        print("\n***********Casal WeWantLearnProgramming************")
        print("code              Dni          Name             Games")
        print("*****************************************************")

        # Realizar búsqueda según el criterio
        for code, student_data in summer_camp_students.items():
            match_found = False  # Bandera para indicar si se encuentra una coincidencia

            if search_criteria == 'dni' and input("Enter the DNI portion to search: ").lower() in student_data[
                'dni'].lower():
                match_found = True

            elif search_criteria == 'name' and input("Enter the name portion to search: ").lower() in student_data[
                'name'].lower():
                match_found = True

            elif search_criteria == 'games':
                games_to_search = input("Enter the games portion to search: ").lower()
                if any(game in games_to_search for game in student_data['games']):
                    match_found = True

            if match_found:
                print("\n********************************Casal WeWantLearnProgramming********************************"
                      "\ncode               Dni                Name                                   Games"
                      "\n********************************************************************************************")
                print(
                    f"{code.ljust(18)} {student_data['dni'].ljust(18)} "
                    f"{student_data['name'].ljust(38)} "
                    f"{', '.join(student_data['games'])}")

                print("********************************************************************************************")

    elif option == "3":
        # Exercici 3 - Codi per llistar usuaris
        print("Listing users...")
        print(summer_camp_students)

    elif option == "4":
        # Sortir del bucle si l'usuari selecciona l'opció 4
        print("Exiting program. Goodbye!")
        break

    else:
        # Missatge d'error si l'usuari introdueix una opció no vàlida
        print("Invalid option. Please choose a valid option.")
