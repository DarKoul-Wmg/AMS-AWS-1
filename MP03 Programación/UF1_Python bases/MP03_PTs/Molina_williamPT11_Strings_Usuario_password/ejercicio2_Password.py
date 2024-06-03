password = ""
pass_valido = True
if len(password)<8: #Longitud minima
    pass_valido = False
    print("menos de 8 caracteres")

if " "in password:
    pass_valido = False
    print("no se permiten espacios en blanco")
#para que tenga un caracter no alfanumerico:
if password.isalnum():
    pass_valido = False
    print("obligatorio un caracter especial")

#minúscules
if password.upper() == password:
    pass_valido = False
    print("Oligatorio una minuscula")

#majúscules
if password.lower() == password:
    pass_valido = False
    print("Oligatorio una majuscula")

#números
contiene_num = False
for letra in password: #Revisa la password en busca de un numero
    if letra.isdigit():#numero
        contiene_num = True
        break
if not contiene_num:
    pass_valido = False
    print("No hay numeros")
if pass_valido:
    print("password válido")
else:
    print("password inválido")
