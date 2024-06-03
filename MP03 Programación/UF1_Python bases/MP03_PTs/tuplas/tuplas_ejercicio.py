menu = 0
lista=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
lista_alumnos = []
while True:
    if menu == 0:
        print("1) Nuevo alumno")
        print("2) Mostrar notas")
        print("3) Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            dni_correcto = False

            nota_correcta = False
#DNI
            while not dni_correcto:
                dni = input("Introduce el dni del alumno:\n")
                if len(dni) != 9:
                    print("longitud incorrecta")
                elif not dni[0:8].isdigit():
                    print("los primeros 8 caraceteres no son digitos")
                elif not dni[8].isupper():
                    print("letra tiene que ser mayuscula")
                elif dni[8] == lista[int(dni[0:8]) % 23]:
                    print("letra dni no es correcta")
                else:
                    print("DNi correcto")
                    dni = dni.upper()
                    dni_correcto = True
            print("DNI verificado")
#NOMBRE
            nombre = input("Introduce el nombre del alumno:\n")
            while not nombre.replace(" ","").isalpha():
                print("Nombre incorrecto")
                nombre = input("Introduce el nombre del alumno:")

            nota = input("Introduce nota:\n")
            while not (nota.replace(".","").isnumeric() and nota.count(".") <= 1 and float(nota) <=10) or nota[0] == ".":
                print("nota incorrecta")
                nota = input("Introduce nota:\n")
            if nota.count(".") != 0:
                nota = float(nota)
                nota = round(nota,2)#NOTAS CON 2 DECIMALES
            else:
                nota = int(nota)
#ORDENAR NOTAS DE MAYOR A MENOR
            for i in range(len(lista_alumnos)):
                if nota > lista_alumnos[i][2]:
                    lista_alumnos.insert(i,(dni,nombre,nota))
                    break
                if i == len(lista_alumnos)-1 and nota < lista_alumnos[i][2]:
                    lista_alumnos.append((dni, nombre, nota))

        elif opcion == 2:
            datos = ""
            for alumno in lista_alumnos:
                nota = alumno[2]

                if str(nota).count(".") == 1:
                    str_nota = str(nota).split(".")[0].rjust(2, "+") + "." + str(nota).split(".")[1].ljust(3, "+")

                else:
                    str_nota = str(nota).rjust(2, "+") + " ".ljust(4, "+")
                datos += alumno[0].ljust(10) + alumno[1].ljust(20) + str_nota + "\n"



        elif opcion == 3:
            print("Cerrando programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")


