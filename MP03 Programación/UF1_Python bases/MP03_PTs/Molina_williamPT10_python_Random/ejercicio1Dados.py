# import random
# print("Se lanzan 2 dados...")
# print("")
#
# print("Primer dado:",random.randint(1,6))
# print("Segundo dado:",random.randint(1,6))
import random
while True:
    d1 = 0
    d2 = 0
    x = input("Quieres tirar los dados? S/N ")
    if (x == "S") or (x == "s"):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print("Ha salido {} y {}".format(d1,d2))
    else:
        break
