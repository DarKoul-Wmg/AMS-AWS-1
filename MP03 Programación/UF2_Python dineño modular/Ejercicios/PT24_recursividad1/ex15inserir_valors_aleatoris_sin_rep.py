import random

def insert_valors_aleatoris_sinrep(num,llista):
    if num == 0:
        return llista
    else:
        llista.append(random.randrange(100))
        if llista[-1] in llista[:-1]:
            llista.remove(llista[-1])
        return insert_valors_aleatoris_sinrep(num-1,llista)




llista = [1,16,8,37,87,91]
num = 10
print(llista)
print(insert_valors_aleatoris_sinrep(num,llista))
