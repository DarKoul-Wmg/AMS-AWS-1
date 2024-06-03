Funcion numOK = es_num_OK (snum,lnum)
	//comprova si el format és correcte dd-mm-yyyy
	numOK = Verdadero
	Para i=1 hasta lnum Hacer
		Si Subcadena(snum,i,i) <> "0"  y Subcadena(snum,i,i) <> "1" y Subcadena(snum,i,i) <> "2" y Subcadena(snum,i,i) <> "3" y Subcadena(snum,i,i) <> "4" y Subcadena(snum,i,i) <> "5" y Subcadena(snum,i,i) <> "6" y Subcadena(snum,i,i) <> "7"  y Subcadena(snum,i,i) <> "8" y Subcadena(snum,i,i) <> "9" Entonces
			numOK = Falso
		FinSi
	FinPara 
FinFuncion
Funcion sepOK = es_separador_OK (separador,separadorAux)
	//comprova si el format és correcte dd-mm-yyyy
	sepOK = Verdadero
	Si separador <> separadorAux Entonces
		sepOK = Falso
	FinSi
FinFuncion

Funcion formatOK = es_format_OK (data)
	//comprova si el format és correcte dd-mm-yyyy
	formatOK = Verdadero
	si Longitud(data) <> 10 Entonces		
		formatOK = Falso
	FinSi
	si formatOK Entonces
		dia = Subcadena(data,1,2)
		//validar dia, són 2 digtis nunérics
		diaOK=es_num_OK (dia,2)
		separador1= Subcadena(data,3,3)
		separador1OK= es_separador_OK(separador1,'-')
		//validar separador
		mes= Subcadena(data,4,5)
		//validar mes, són 2 digtis nunérics
		mesOK=es_num_OK (mes,2)
		separador2= Subcadena(data,6,6)
		separador2OK= es_separador_OK(separador2,'-')
		//validar separador
		any=Subcadena(data,7,10)
		//validar any, són 4 digtis nunérics
		anyOK=es_num_OK (any,4)
		si no diaOK o no separador1OK o no mesOK o no separador2OK o no anyOK Entonces
			formatOK = Falso
		FinSi
	FinSi
FinFuncion

Funcion diaOK = es_dia_OK (any, mes, dia) 
	//comprova dia
	diaOK=Verdadero
	si dia < 0 o dia > 31 Entonces
		diaOK=Falso
	SiNo
		si mes = 4 o mes = 6 o mes = 9 o mes =11 Entonces
			si dia > 30 entonces
				diaOK=Falso
			FinSi
		FinSi
		si mes = 2 Entonces
			si dia > 29 entonces
				diaOK=Falso
			FinSi
		FinSi
	FinSi
FinFuncion

Funcion mesOK = es_mes_OK (mes) 
	//comprova mes
	mesOK = Falso
	si mes>=0 y mes<=12 Entonces
		mesOK = Verdadero
	sino 
		mesOK = Falso
	FinSi	
FinFuncion

Funcion anyOK = es_any_ok (any) 
//comprova any
	anyOK = Verdadero
	si any < 0 o any > 2030
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
		dia=ConvertirANumero(Subcadena(data,1,2))
		mes=ConvertirANumero(Subcadena(data,4,5))
		any=ConvertirANumero(Subcadena(data,7,10))
		//validar any, ha de ser un valor entre 0 i 2023
		dataOK=es_any_OK (any) 
		//validar mes, ha de ser un valor entre 1 i 12
		si dataOK Entonces
			dataOK=es_mes_OK (mes) 
		FinSi
		//validar dia, ha de ser un valor entre 1i 31
		si dataOK Entonces
			dataOK=es_dia_ok (any,mes,dia)
		FinSi
	FinSi
	
	//si la data es OK mostrem e missatge corresponent
	si dataOK entonces
		Escribir "La data introduïda: " data " és valida"
	sino
		Escribir "La data introduïda: " data " NO és valida"
	FinSi
FinAlgoritmo
