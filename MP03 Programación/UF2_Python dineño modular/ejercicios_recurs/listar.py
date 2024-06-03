def ex3(titol,**productos):
    print("{}".center(62,"=").format(titol))
    print("Item".ljust(20) + "Amount".rjust(15) + "Price".rjust(15) + "Total".rjust(15))
    try:
        total = 0
        for id, producto in productos.items():
            if not isinstance(producto, list):
                raise ValueError("The values have to be a list of integers")

            if len(producto) != 2:
                raise AssertionError("The list have to contain only two integers")
            for elemento in producto:
                if not isinstance(elemento, int):
                    raise TypeError("Values in list have to be integers")

            amount = producto[0]
            price = producto[1]
            item_total = price * amount
            total += item_total

            print(str(id).ljust(20) + str(amount).rjust(15) + str(price).rjust(15) + str(item_total).rjust(15))

        print("="*65)
        print("total".ljust(50) + str(total).rjust(15))

    except Exception as error:
        print(error)
        quit()

ex3("Titol")
ex3("Titol", RT345=[2,145])
ex3("Titol", RT345=[2,145], SW432=[5,549])
ex3("Titol", RT345=[2,145], SW432=[5,549],OT441=[4, 299])
