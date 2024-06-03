
#Para utilizar Break se necesita estar en un bucle while
while True:

 print("CALCULADORA")
 print("Menu Principal")
 print("    ")
 print("1 - Sumar")
 print("2 - Restar")
 print("3 - Multiplicar")
 print("4 - Dividir")
 print("0 - Sortir")
 print("    ")

 option = input("Opció:")



#Suma
 if option == "1":
    num1 = float(input("Tria el primer numero:"))
    num2 = float(input("Ara tria el segon numero:"))
    print("La suma dels dos números es: " + str(num1 + num2))
    print("    ")


#Resta
 elif option == "2":
    num1 = float(input("Tria el primer numero:"))
    num2 = float(input("Ara tria el segon numero:"))
    print("La resta dels dos números es: " + str(num1 - num2))
    print("    ")


#Multiplicació
 elif option == "3":
    num1 = float(input("Tria el primer numero:"))
    num2 = float(input("Ara tria el segon numero:"))
    print("La multiplicació dels dos números es: " + str(num1 * num2))
    print("    ")


#Divisió
 elif option == "4":
    num1 = float(input("Tria el primer numero:"))
    num2 = float(input("Ara tria el segon numero:"))
    if num2 == 0:
        print("Error: El segon numero no pot ser 0.")
    else:
     print("La divisió dels dos números es: " + str(num1 / num2))
     print("    ")


#Sortir
 elif option == "0":
    break

