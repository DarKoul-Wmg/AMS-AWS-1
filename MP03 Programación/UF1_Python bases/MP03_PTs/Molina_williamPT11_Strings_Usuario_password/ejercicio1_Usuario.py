usuario=""
usuariovalido = True
if len(usuario) < 6:
    print("Usuario tiene que tener almenos 6 caracteres")
    usuariovalido = False
if len(usuario) > 12:
    print("Usuario tiene que tener menos de 12 caracteres")
    usuariovalido = False
if not usuario.isalnum():
    print("El nom només pot tenir numeros i lletres")
    usuariovalido = False
if not usuariovalido:
    print("Usuario no valido")
else:
    print("usuario válido")
