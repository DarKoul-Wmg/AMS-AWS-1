Algoritmo CalcularAnyoBisiesto
	Definir anyo1, anyo2, anyoIni, anyoFin como entero
	
	Escribir "Introduce el primer año:"
	Leer anyo1
	Escribir "Introduce el segundo año:"
	Leer anyo2
	
	Mientras anyo1 <= 0 o anyo2 <= 0
		Escribir  "Los años deben ser mayores que 0. Vuelve a seleccionar años:"
		Escribir  "Introduce el primer año:"
		Leer anyo1
		Escribir  "Introduce el segundo año:"
		Leer anyo2
	FinMientras

	Si anyo1 < anyo2 Entonces
		anyoIni <- anyo1
		anyoFin <- anyo2
	SiNo
		anyoIni <- anyo2
		anyoFin <- anyo1
	FinSi
	
	Escribir "Años bisiestos entre ", anyoIni, "y",  anyoFin, ":"
	Para i <- anyoIni Hasta  anyoFin Con Paso 1 Hacer
		Si (i MOD 4 = 0 Y (i MOD 100 <> 0 o i MOD 400 = 0)) Entonces
			Escribir i

		FinSi
	FinPara
FinAlgoritmo
