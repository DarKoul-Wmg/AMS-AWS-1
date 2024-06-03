def divisors(num):
    lista_divisores = []
    for i in range(1,num+1):
        if num % i == 0:
            lista_divisores.append(i)

    return lista_divisores

num = int(input("Introduce un numero"))
resultado = divisors(num)
print("Divisores de {}: ".format(num))
for divisor in resultado:
    print(divisor)


