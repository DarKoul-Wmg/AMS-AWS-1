Algoritmo Multiples_Intervalo_Dado
	Definir i, f, sum5, sum10, mult5, mult10 Como Entero 
	Escribir "Numero inicial"
	Leer i
	Escribir "Numero final"
	leer f
	
	Mientras f <= i Hacer
		Escribir "Dime otro numero final mas grande que el anterior"
		leer f
	FinMientras
	
	mult5 = 0
	mult10 = 0
	sum5 = 0
	sum10 = 0
	
	Mientras i <= f Hacer
		Si i % 5 == 0 Entonces
			mult5 = mult5 + 1
			sum5 = sum5 + i
			
		FinSi
		Si i%10 ==0 Entonces
			mult10 = mult10 + 1
			sum10 = sum10 + i
		FinSi
		i = i +1
	FinMientras
	Escribir "Multiples de 5 entre " i " - " f " son: " mult5 " i la suma es: " sum5
	Escribir "Multiples de 10 entre " i " - " f " son: " mult10 " i la suma es: " sum10
FinAlgoritmo
