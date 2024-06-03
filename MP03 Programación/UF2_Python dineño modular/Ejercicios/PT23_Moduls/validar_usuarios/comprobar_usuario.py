def usuario_Valido(nombre):
    usuario = True

    if len(nombre) < 6:
        usuario = False
        return print("El nom d'usuari ha de contenir almenys 6 caràcters")

    if len(nombre) > 12:
        usuario = False
        return print("El nom d'usuari no potcontenir més de 12 caràcters")

    if not nombre.isalnum():
        usuario = False
        return print("El nom d'usuari pot contenir només lletres i números")

    else:
        return True



resultado = usuario_Valido("anni3ii")

print(resultado)
