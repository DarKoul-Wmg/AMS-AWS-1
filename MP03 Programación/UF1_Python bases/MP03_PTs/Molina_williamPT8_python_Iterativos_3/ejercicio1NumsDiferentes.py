while True:
 totalnums = int(input("Cantidad de numeros a introducir: "))

 if totalnums <= 0:
  print("Introduce un valor positivo...")

 else:
  break

num_anterior = int(input("Dame el primero valor:"))
for numero in range(totalnums):

  num = int(input(f"Dame un numero diferente a {num_anterior}: "))

  if num_anterior == num:
   print("Dame un numero que no sea",num,":")
   num -= 1 #Para volver al anterior resultado.


  else:
   num_anterior = num

print("Gracias por su colaboración")




