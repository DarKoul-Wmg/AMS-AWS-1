palabra1 = input("Dime una palabra:")
palabra2 = input("Dime una palabra:")
palabra3 = input("Dime una palabra:")
palabra4 = input("Dime una palabra:")
palabra5 = input("Dime una palabra:")

palabra_menor = palabra1

if palabra2 < palabra_menor:
    palabra_menor = palabra2

if palabra3 < palabra_menor:
    palabra_menor = palabra3

if palabra4 < palabra_menor:
    palabra_menor = palabra4

if palabra5 < palabra_menor:
    palabra_menor = palabra5

print(palabra_menor)

