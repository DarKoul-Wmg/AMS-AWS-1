Funcion formatOK = es_format_OK (data)
	//comprova si el format és correcte dd-mm-yyyy
	formatOK = Verdadero
	si Longitud(data) <> 10 Entonces	
		//Comprova que la data no tingui més de 10 caracters
		formatOK = Falso
	FinSi
	si formatOK Entonces
		dia = Subcadena(data,1,2)
		//validar dia, són 2 digtis numérics
		separador1= Subcadena(data,3,3)
		//validar separador
		mes= Subcadena(data,4,5)
		//validar mes, són 2 digtis numérics
		separador2= Subcadena(data,6,6)
		//validar separador
		anyo=Subcadena(data,7,10)
		//validar any, són 4 digtis numérics
	FinSi
FinFuncion

Funcion diaOK = es_dia_OK (any, mes, dia) 
	//comprova dia
	diaOK = Falso
	si dia>=1 y dia<=31 Entonces
		//Comprova que dia sigui un valor entre 1 i 31
		diaOK = Verdadero
	Sino 
		si mes = 4 o mes = 6 o mes = 9 o mes = 11 Entonces
			si dia = 31 Entonces
				diaOK = Falso
			FinSi
		FinSi
		si mes = 2 Entonces
			si dia > 29 Entonces
				diaOK = Falso
			FinSi
		FinSi
	FinSi

FinFuncion

Funcion mesOK = es_mes_OK (mes) 
	//comprova mes
	mesOK = Falso
	si mes>=1 y mes<=12 Entonces
		//Comprova que mes sigui un valor entre 1 i 12 
		
		mesOK = Verdadero
		
	 //Eliminació de la condició Sino (el bool ja es trova en Falso)
	FinSi	 
FinFuncion

Funcion anyOK = es_any_OK (any) 
//comprova any
	anyOK = Verdadero
	si anyo < 0 y anyo > 2023 Entonces
		//Comprova que any no sigui negatiu o 0.
		anyOK = Falso
	FinSi
FinFuncion

Funcion data <- llegir_entrada (primera_vegada)
	//demana introduir un valor, mostra un missatge diferent segons si es la primera vegada o no 
	si primera_vegada Entonces
		Escribir "Introdueix una data 0 per acabar"
	SiNo
		Escribir "Introdueix un nova data, el format de la data anterior no era correcte, si no vols continuar entra 0"		
	FinSi
	Leer data
FinFuncion


Algoritmo principal
	// demanen que si introdueixi una data els formats valids són : dd-mm-yyyy 
	// verdadero vol dir que es primera vegada
	Definir data como cadena;
	data = llegir_entrada (Verdadero) 
	Escribir data
	dataOK = Falso
	entrada0 = Falso
	
	//mentre no s'introdueix una data amb format vàlid o 0 es demana que s'introdueixi una data
	mientras no dataOK Y no entrada0 hacer
		si data="0" entonces
			entrada0=Verdadero
		SiNo
			dataOK = es_format_OK (data)
			si no dataOK entonces 
				data <- llegir_entrada (Falso) 
			FinSi
		FinSi
	FinMientras
	
	//si la data es OK en format validem si es una data correcte
	si dataOK entonces
		dia = ConvertirANumero(Subcadena(data,1,2))
		mes= ConvertirANumero(Subcadena(data,4,5))
		anyo=ConvertirANumero(Subcadena(data,7,10))
		//validar any, ha de ser un valor entre 0 i 2023
		si dataOK Entonces
			dataOK=es_any_OK (any) 
		FinSi
		//validar mes, ha de ser un valor entre 1 i 12
		si dataOK Entonces
			dataOK=es_mes_OK (mes) 
		FinSi
		//validar dia, ha de ser un valor entre 1i 31
		si dataOK Entonces
			dataOK=es_dia_OK (any,mes,dia)
		FinSi
	FinSi
	
	//si la data es OK mostrem e missatge corresponent
	si dataOK entonces
		Escribir "La data introduida: " data " és valida"
	sino
		Escribir "La data introduida: " data " no és valida"
	FinSi
FinAlgoritmo
