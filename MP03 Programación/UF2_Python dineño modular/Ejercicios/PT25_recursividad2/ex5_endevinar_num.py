import random
def adivinar_num(num,min=0,max=1000): #pasar como argumentos obligatorios para que se actualicen los valores.
    intentos = 0
    resultado = int(input("Cual es? "))
    if resultado == num:
        intentos += 1
        return intentos
        #print("CORRECTO, lo has adivinado en: {} intentos.".format(intentos))

    else:
        if resultado < num:
            min = resultado
            print("Numero entre {} y {}".format(min,max))
        elif resultado > num:
            max = resultado

            print("Numero entre {} y {}".format(min,max))
        intentos += 1
        return intentos + adivinar_num(num,min,max)


print("El programa ha generado un numero entre el 0 y el 1000")

intentos = adivinar_num(num=random.randint(0,1000))
print("CORRECTO, lo has adivinado en: {} intentos.".format(intentos))
