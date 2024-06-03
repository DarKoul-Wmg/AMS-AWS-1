#EX 1

def sumar(num1,num2):
    resultat = num1 + num2
    return resultat

def restar(num1,num2):
    resultat = num1 - num2
    return resultat

def multiplicar(num1,num2):
    resultat = num1 * num2
    return resultat

def dividir(numerador,denominador):

    try:
        if denominador == 0:
            raise ZeroDivisionError("ERROR: No es pot dividir per zero")

        resultat = numerador / denominador
        return resultat

    except ZeroDivisionError as error:
        print(error)



