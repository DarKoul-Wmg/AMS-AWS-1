import random
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
aleatorio = []

for i in range(10):
    aleatorio.append(abecedario[random.randint(0,25)])

print(aleatorio)

