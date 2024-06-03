usuario = input("Introduce tu nombre de usuario: ")
usuariovalido = True
if len(usuario) < 6:
    print("Usuario tiene que tener almenos 6 caracteres")
    usuariovalido = False
if len(usuario) > 12:
    print("Usuario tiene que tener menos de 12 caracteres")
    usuariovalido = False
if not usuario.isalnum():
    print("El nombre solo puede tener numeros y letras")
    usuariovalido = False
if not usuariovalido:
    print("Usuario no valido")
else:
    print("usuario válido")
print("\n \n")

if usuariovalido == True:
    password = input("Ahora dime una contraseña para tu usuario: ")
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
      print("Obligatorio que contenga un numero")
    if pass_valido:
     print("password válido")
    else:
        print("password inválido")
