
lista=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
dni = int(input("Introduce las letras del dni para calcular la letra: "))

letra = lista[dni %23]

print(letra)
