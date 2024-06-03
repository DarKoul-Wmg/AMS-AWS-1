import random

def insert_valors_aleatoris(num,llista):
    if num == 0:
        return llista
    else:
        llista.append(random.randrange(100))
        return insert_valors_aleatoris(num-1,llista)




llista = [1,16,8,37,87,91]
num = 5
print(llista)
print(insert_valors_aleatoris(num,llista))
