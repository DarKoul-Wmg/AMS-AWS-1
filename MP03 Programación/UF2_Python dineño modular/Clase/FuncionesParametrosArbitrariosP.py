
##parametros con nombre

def funcion(parametro1,parametro2 = 'valorpordefecto2'):
    print('Parametro = {}, parametro2 = {}'.format(parametro1,parametro2))

funcion('AAAAAAA','BBBBBB')

##Funcion con dos parametros y se puede omitir uno de ellos

funcion(parametro2='AAAAAAA',parametro1='BBBBBBB')



#####python introduce los elementos en una tupla con la funcion: (*)

def suma_numeros(par1,par2,*par3):
    print('par1 =',par1)
    print('par2 =', par2)
    print('par3 =', par3)
    print(type(par3))
    suma = par1+par2

    for elemento in par3: #par 3 es una tupla
        suma += elemento
    print('suma= ',suma)


suma_numeros(1,2)
print('***********************************')
suma_numeros(1,2,3)
print('***********************************')
suma_numeros(1,2,3,4)
print('***********************************')
suma_numeros(1,2,3,4,5)


####almacenar cosas en un diccionario



def parametros_arbitrarios(**par3):
    print(par3)
parametros_arbitrarios()
print('***********************************')

parametros_arbitrarios(nombre='pepe',apellidos='lopez fuentes')
