Algoritmo JuegoAdivinaNumero
    // Men� principal
    Repetir
        Escribir "Men�:"
        Escribir "1 - Jugar"
        Escribir "2 - Salir"
        Escribir "Elija una opci�n:"
        Leer opcion
		
        Segun opcion Hacer
            1:
                JugarAdivinaNumero()
            2:
                Escribir "Saliendo del programa."
            De Otro Modo:
                Escribir "Opci�n no v�lida. Intente de nuevo."
        FinSegun
    Hasta Que opcion = 2
FinAlgoritmo

SubAlgoritmo JugarAdivinaNumero
    // Inicializaci�n
    Definir intentos, num_secreto, num_ingresado Como Entero
    intentos = 0
    num_secreto = azar(100)+1

    // Solicitar el n�mero m�ximo de intentos
    Mientras (intentos < 1 O intentos > 10) Hacer
        Escribir "Introduzca el n�mero m�ximo de intentos (entre 1 y 10):"
        Leer intentos
        Si (intentos < 1 O intentos > 10) Entonces
            Escribir "N�mero de intentos no v�lido. Intente de nuevo."
        FinSi
    FinMientras
    
    // Juego
    Escribir "Adivine el n�mero (de 1 a 100):"
    Leer num_ingresado
    
    Mientras (num_secreto <> num_ingresado Y intentos > 1) Hacer
        Si (num_secreto > num_ingresado) Entonces
            Escribir "Muy bajo"
        Sino
            Escribir "Muy alto"
        FinSi
        
        intentos <- intentos - 1
        Escribir "Le quedan ", intentos, " intentos."
        Escribir "Introduzca un n�mero:"
        Leer num_ingresado
    FinMientras
    
    // Resultado del juego
    Si (num_secreto = num_ingresado) Entonces
        Escribir "�Exacto! Usted adivin� el numero a falta de: ",intentos, " intentos."
    Sino
        Escribir "El n�mero era: ", num_secreto
    FinSi
FinSubAlgoritmo