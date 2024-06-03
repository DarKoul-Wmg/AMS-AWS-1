Algoritmo JuegoAdivinaNumero
    // Menú principal
    Repetir
        Escribir "Menú:"
        Escribir "1 - Jugar"
        Escribir "2 - Salir"
        Escribir "Elija una opción:"
        Leer opcion
		
        Segun opcion Hacer
            1:
                JugarAdivinaNumero()
            2:
                Escribir "Saliendo del programa."
            De Otro Modo:
                Escribir "Opción no válida. Intente de nuevo."
        FinSegun
    Hasta Que opcion = 2
FinAlgoritmo

SubAlgoritmo JugarAdivinaNumero
    // Inicialización
    Definir intentos, num_secreto, num_ingresado Como Entero
    intentos = 0
    num_secreto = azar(100)+1

    // Solicitar el número máximo de intentos
    Mientras (intentos < 1 O intentos > 10) Hacer
        Escribir "Introduzca el número máximo de intentos (entre 1 y 10):"
        Leer intentos
        Si (intentos < 1 O intentos > 10) Entonces
            Escribir "Número de intentos no válido. Intente de nuevo."
        FinSi
    FinMientras
    
    // Juego
    Escribir "Adivine el número (de 1 a 100):"
    Leer num_ingresado
    
    Mientras (num_secreto <> num_ingresado Y intentos > 1) Hacer
        Si (num_secreto > num_ingresado) Entonces
            Escribir "Muy bajo"
        Sino
            Escribir "Muy alto"
        FinSi
        
        intentos <- intentos - 1
        Escribir "Le quedan ", intentos, " intentos."
        Escribir "Introduzca un número:"
        Leer num_ingresado
    FinMientras
    
    // Resultado del juego
    Si (num_secreto = num_ingresado) Entonces
        Escribir "¡Exacto! Usted adivinó el numero a falta de: ",intentos, " intentos."
    Sino
        Escribir "El número era: ", num_secreto
    FinSi
FinSubAlgoritmo