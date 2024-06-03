def contrasenya_Valida(contrasenya):
    passwd = True

    if len(contrasenya) < 8:
        passwd = False

    if contrasenya.upper() == contrasenya or contrasenya.lower() == contrasenya:#Minujscula y #Majuscula
        passwd = False


    if contrasenya.isalnum(): #No alphanum
        passwd = False

    #Numero
    num = False
    for caracer in contrasenya:
        if caracer.isdigit():
            num = True
            break
    if not num:
        passwd = False

    if ' ' in contrasenya:
        passwd = False

    return passwd

resultado = contrasenya_Valida("Wil@04")

print(resultado)

