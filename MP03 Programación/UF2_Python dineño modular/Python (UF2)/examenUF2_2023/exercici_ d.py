def exercici2(*numbers):
    # Comprovació del nombre d'arguments.
    if len(numbers) < 2:
        raise ValueError("Només dos nombres.")

    total = 0
    count = 0

    for num in numbers:
        # Comprovació si cada element és un enter positiu.
        if not isinstance(num, int) or num <= 0:
            raise TypeError("Números positius, si us plau.")

        total += num
        count += 1

    # Càlcul de la mitjana.
    average = total / count
    return average

# Exemples d'ús erronis:
try:
    # Generarà un error perquè no hi ha prou arguments.
    print(exercici2())
except ValueError as ve:
    print(ve)

try:
    # Generarà un error perquè no hi ha prou arguments.
    print(exercici2(1))
except ValueError as ve:
    print(ve)

try:
    print(exercici2("a", 1, 2))  # Generarà un error de tipus:
except TypeError as te:
    print(te)

# Aquests exemples sí que funcionen. :)
print(exercici2(1, 2))
print(exercici2(1, 2, 3))
print(exercici2(1, 2, 3, 4, 5))
