copia = open("archivo2","a+")

with open("archivo1","r") as original:
     datos = original.readlines()
     for dato in datos:
         print(dato)
         copia.write(dato)


copia.close()
