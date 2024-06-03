def exercici3(title, *items):
    print("=" * 30 + title + "=" * 30)
    print("Item".ljust(20) + "Amount".rjust(15) + "Price".rjust(15) + "Total".rjust(15))
    print("=" * 65)

    total_amount = 0
    total_cost = 0

    for item, values in items:
        if not (isinstance(values, list) and len(values) == 2 and all(isinstance(v, int) for v in values)):
            print("Error: Invalid input. Please provide a list of two integers.\n\n")
            return

        quantity, price_per_unit = values
        total = quantity * price_per_unit

        print(item.ljust(20) + str(quantity).rjust(15) + str(price_per_unit).rjust(15) + str(total).rjust(15))

        total_amount += quantity
        total_cost += total

    print("=" * 65)
    print("Total".ljust(50) + str(total_cost).rjust(15))
    print("\n")

# Ejemplos de uso
exercici3("Titol")
exercici3("Titol", ("RT345", [2]))
exercici3("Titol", ("RT345", [2, 145]))
exercici3("Titol", ("RT345", [2, 145]), ("SW432", [5, 549]), ("RERER2421421", [20, 20000]))
