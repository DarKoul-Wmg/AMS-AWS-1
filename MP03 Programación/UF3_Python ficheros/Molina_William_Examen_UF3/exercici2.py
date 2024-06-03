import random

letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'
    ,'S','T','U','V','W','X','Y','Z']

def id_nuevo():
    id_nuevo = ""
    id_nuevo += letras[random.randint(0,26)]
    id_nuevo += letras[random.randint(0,26)]
    id_nuevo += str(random.randint(0,9))
    id_nuevo = "TS7"
    return id_nuevo

def exercici2(dictClient):
    fichero = open("clients.txt","a+")

    #print(id_nuevo)

    for clave in dictClient:
        #print(clave)
        if clave.lower() == "name":
            nombre = dictClient[clave]
        if clave.lower() == "surname1":
            apellido1 = dictClient[clave]
        if clave.lower() == "surname2":
            apellido2 = dictClient[clave]
        if clave.lower() == "dni":
            dni = dictClient[clave]
        if clave.lower() == "tfn":
            tfn = dictClient[clave]
        if clave.lower() == "age":
            edad = dictClient[clave]
    surnames = apellido1+"-"+apellido2
    id = id_nuevo()
    datos = "\nName: "+nombre+ ";" +"  id:"+id+ " ;" +" surnames: "+surnames+ ";" +"age: "+edad+ ";" +"   dni:"+dni+ ";" \
            +"  tfn: "+tfn
    print(datos)
    fichero.write(datos)
    print("Datos introducidos")
    fichero.close()


dictClient = {'name':'Sebastian','surname1':'Almansa','surname2':'Navarro'
             ,'dni':'77777777G','tfn':'767676767','age':'34'}

exercici2(dictClient)
