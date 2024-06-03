import math
# 3. Implementar un programa que permeti:
# a) Calcular el perímetre i àrea d’un rectangle donat la seva base i la seva alçada.
#          El perímetre, L, d'un rectangle de base b i altura h és: L = 2*b + 2*h
#          L'àrea, d'un rectangle de base b i altura h és: S =b*h

# b) Calcular el perímetre i àrea d’un cercle donat el seu radi.
# A= PI*r^2 (àrea d’un cercle de radi r)
# P= 2*PI*r(Perímetre d’un cercle de radi r)

# c) Calcular el volum d’una esfera donat el seu radio.
# V=4/3 * PI^3 (Volum d’una esfera de radi r)

# a)
print("Calcular perímetre i àrea d'un rectangle. En primer lloc posa el valor de la base ")
b = int(input())

print("Posa el valor de la altura")
h = int(input())
print('\n     \n')
L = 2 * b + 2 * h
S = b * h
print("El perimetre del rectangle es "+ str(L))
print("L'àrea del rectangle es "+ str(S))

# b)
print('\n     \n')
print("Calcular el perímetre i àrea d’un cercle. Dona'm el seu radi: ")
r = int(input())

A = float(math.pi * math.pow(r,2))
P = 2 * math.pi * r
print("El perímetre del cercle es " + str(P))
print("L'àrea del cercle es " + str(A))

# c)
print('\n     \n')
print("Donat el radi anterior, calcularem el volum d'una esfera")

V = (4/3)*float(math.pi * math.pow(r,3))

print("El volum de la esfera es " + str(V))
