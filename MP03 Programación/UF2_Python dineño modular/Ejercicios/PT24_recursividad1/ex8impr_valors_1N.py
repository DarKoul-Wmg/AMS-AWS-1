def imprimir_valores(n):
    if n == 0:
        return n
    else:
        imprimir_valores(n-1) #Influye en el orden de printear
        print(n)

n = 10
imprimir_valores(n)

# def imprimir_valores(n):
#     resultado = 1
#     if resultado == n:
#         return n
#     else:
#         print(n)
#         return imprimir_valores(n-1)
#
#
# n = 10
# print(imprimir_valores(n))
