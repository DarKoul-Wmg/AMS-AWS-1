correos = ["hola1@23.COM","a4@@b.com", ".a.b3@c.com","asef..asdf@asef.com","awer@wer.commmm","a.b1@c.d.es","a.b2@c.com"]
# correo = input("Introduce una dirección de correo y te la valido: ")
cadena = ""
resultado = []
alnum = False
nom_corr = True
dom_corr = False
arroba = True
# nombre = ""
# dominio = ""
for correo in correos:
    cont_arroba = correo.count("@")
    if cont_arroba >= 2 or cont_arroba == 0:
     arroba = False
     if arroba == False:
        nom_corr = False
        dom_corr = False
        # print("El correo tiene que contener una @")

    separar = correo.find("@")
    if separar != -1:  #Detectar si @ se encuentra en correo
     nombre = correo[:separar]  #Obtener el nombre
     #print(nombre)
     dominio = correo[separar + 1:] #Obtener el dominio
     #print(dominio)

     #RESTRICCIONES DEL CORREO:

    if ".." in correo or " " in correo:
         alnum = False
         #print("El nombre del correo no es valido al tener un espacio en blanco o ..")

    if nombre.isalnum():
         for d in dominio: #Comprobación de los caracteres permitidos: isalum y "."
             if d.isalnum() or d == ".":
                alnum = True
             else:
                 alnum = False
    #Nombre empieza por "."
    if nombre[0] == ".":
        nom_corr = False

    #Dominio restringido a 2-3 caracteres al final:
    if dominio[len(dominio)-4]==".":
        dom_corr = True
    if dominio[len(dominio)-3] == ".":
        dom_corr = True
    #Montar cadena para el resultado
    if nom_corr == True and dom_corr == True and alnum == True:
        cadena += "Nombre: " + nombre + " Dominio: "+ dominio +"\n"
    dom_corr = False
    nom_corr = True

print("Los correos correctos son: \n" + cadena)

