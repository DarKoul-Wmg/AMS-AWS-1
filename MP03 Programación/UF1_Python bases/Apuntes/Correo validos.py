# #Formato: alnum.alnum.alnum@alnum.alnum.alnum(el ultimo long 2 o 3)
# #mails = [".@asref.com", "asef..asdf@asef.com", ".asf@asdf.com", "asdf..@awe.com", "asdf..@awe.com"
#     #, "sdfsdf@awe.com.", "sdfsdf@.awe.com", "sdfsdf@awe..com" ,"awer@wer.com","awer@wer.commmm"]
# #mails_correctos
# mails = ["a@b.com, a.b@c.com","a.b@c.com","a.b@c.d.es, ashf.fjgk@mhkgl.goho.com"]
# #de 0 a @ es el nombre, y de @ al final es el dominio
# #Hacer preguntas (mas grande que 0?, eres alnum?), al ultimo, como tiene que llegar entre long 2 y 3 se le pregunta la longitud al ultimo.
# #dom =alnum.alnum.alnum "."
# for mail in mails:
#     print(mail) #consigo los mails 1 por 1
#     inicio = 0
#     count = mails.count(".")
#     index = 0
#     if inicio ==0:
#         inicio = 0
#         final = mail.index('.')
#         for i in range(count):
#             final = mail.index(".", inicio)
#             nombre = mail[inicio:final]
#             index += 1
#             print(f"{index}: {nombre}")
#             inicio = final + 1
#         nombre_final = mail[inicio: ]
#         index += 1
#         print(f"{index}:{nombre_final}")


correos = ["a4@@b.com", ".a.b3@c.com","a.b2@c.com","a.b1@c.d.es","awer@wer.commmm","asef..asdf@asef.com"]
# correos = input("validar correo:")
cadena = ""
resultado = []
alnum = False
nom_corr = True
dom_corr = False


for correo in correos:
    separar = correo.find("@")
    if separar != -1: #Detectar si @ se encuentra en correo
     nombre = correo[:separar] #Obtener el nombre
     #print(nombre)
     dominio = correo[separar + 1:] #Obtener el dominio
     #print(dominio)

     #RESTRICCIONES DEL CORREO:
     if "@" == 0:
         alnum = False

     if ".." in correo or " " in correo:
         alnum = False
         #print("El nombre del correo no es valido al tener un espacio en blanco o ..")

     if nombre.isalnum():
         for d in dominio: #Comprobación de los caracteres permitidos: isalum y "."
             if d.isalnum() or d == ".":
                alnum = True
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
