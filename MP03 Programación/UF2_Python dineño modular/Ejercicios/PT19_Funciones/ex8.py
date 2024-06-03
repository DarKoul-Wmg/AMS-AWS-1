def anysTraspas():
    any1 = int(input("Primer any"))
    any2 = int(input("Segon any (posterior)"))
    while not any1 < any2:
        any2 = int(input("{} no es major que {}, torna a introduir un any: ").format(any2,any1))

    anyTra = 0
    anysTot = 0

    for any in range(any1, any2 +1):
        anysTot +=1

        if any %4==0 and (any%400 == 0 or any%100 != 0):
            anyTra += 1

    print("Entre els anys {}-{} hi ha {}, on {} són de traspàs".format(any1,any2,anysTot,anyTra))

anysTraspas()
