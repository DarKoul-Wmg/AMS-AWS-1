palabra1 = input("Dime una palabra:")
palabra2 = input("Dime una palabra:")
palabra3 = input("Dime una palabra:")
palabra4 = input("Dime una palabra:")
palabra5 = input("Dime una palabra:")

palabra_menor = palabra1

if palabra2.lower() < palabra_menor.lower():
    palabra_menor = palabra2

if palabra3.lower() < palabra_menor.lower():
    palabra_menor = palabra3

if palabra4.lower() < palabra_menor.lower():
    palabra_menor = palabra4

if palabra5.lower() < palabra_menor.lower():
    palabra_menor = palabra5

print(palabra_menor)
