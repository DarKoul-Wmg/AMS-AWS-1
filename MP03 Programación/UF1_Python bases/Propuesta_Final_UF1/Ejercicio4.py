import random
letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
print("Algorisme dni aleatori i vàlid:")
input("Enter per generar el dni:")
dni_num =''
for i in range(8):
    dni_num += str(random.randint(1,9))

dni = dni_num + letrasDni[int(dni_num)%23]

print(dni)
