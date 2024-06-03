# #2. Escriure un programa que pregunti a l’usuari:
#  a) El seu nom, i després saludi.
#  b) dos números i després mostri el producte.

# a)
print("Cuál es tu nombre")
nom = input()

print("Buenas, encantado de conocerte " + nom)

# b)
print(nom + " me puedes dar dos numeros para que te muestre el producto de estos?")
print("Dime el primer numero")
num1 = int(input())
print("Ahora dime el segundo")
num2 =  int(input())
producte = num1 * num2

print("El producto de los dos numeros dados es "+ str(producte))
