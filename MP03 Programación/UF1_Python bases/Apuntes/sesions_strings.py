
cadena = "asdf ASDF asdf asdf asdf asdf "

cadena = "    asdfsfq;asdsadqw     ;asdfqwer;    asadfqwer  "

#print(cadena[2:]) ==> dfsfq;asdsadqw;asdfqwer;asadfqwer
#print(cadena[:10]) ==> asdfsfq;as
#cadena = "abcd"

#Con cadena no se traducen a minusculas, es necesario crear cadena2 para que funcione (tambien sirve con cadena.lower())
#cadena2 = cadena.lower()
# print(cadena2) = asdf asdf asdf asdf asdf asdf

#lo mismo pasa con cadena.upper
#cadena2 = cadena.upper()
#print(cadena2) = ASDF ASDF ASDF ASDF ASDF ASDF

#.............................................

#Alfanumérico:
#cadena2 = cadena.isalnum() ====> isapha solo da true con letras
#print(type(cadena2))
#print(cadena2)
#print(cadena)

#cadena2 = cadena.isdigit() ====> Utilizado en menús, solo con num
#print(type(cadena2))
#print(cadena2)
#print(cadena)

#cadena2 = cadena.isspace() ====> True cuando cadena contiene espacios
#print(type(cadena2))
#print(cadena2)
#print(cadena)

#cadena2 = cadena.capitalize() ==> primera letra en may


#cadena2 = cadena.center(30,"-") ==> -------------WEWE-------------

# cadena2 = cadena.find("WE") ==>7      2323535WEWE

# cadena2 = cadena.find("WE",10) DONDE EMPEZAR A BUSCAR (10) ===> 11    2323535WEWEWEWEWEWEAAA

#cadena2 = cadena.find("AA",10,20) ===> -1
# 2323535WEWEWEWEWEWEAAA    No encontrado

#cadena2 = cadena.startswith("AA")  ==> <class 'bool'> False 2323535WEWEWEWEWEWEAAA no empieza en AA
#cadena2 = cadena.endswitch ("AA")  ==> True

#cadena2 = cadena.count("AA",5,20)

# ILEGAL USAR DE MOMENTO ===
#cadena = "asdfsf;asdsad;asdf;asadf"
#  cadena2 = cadena.split(";") ===> <class 'list'>
#  ['asdfsf', 'asdsad', 'asdf', 'asadf']
#   asdfsf;asdsad;asdf;asadf


#cadena2 = cadena.replace("as","**",2) ===> **dfsf;**dsad;**df;**adf
#asdfsf;asdsad;asdf;asadf
# SI 2=-1, reemplaza todas por defecto

print(len(cadena)) #Te enseña el numero de caracteres en la cadena


#print(cadena[len(cadena)-1]) ==> 4 d

#print(cadena[2:8]) ==> dfsfq;
#print(cadena[9]) ==> s
  #print(cadena[2:]) ==> dfsfq;asdsadqw;asdfqwer;asadfqwer
  #print(cadena[:10]) ==> asdfsfq;as

#print(cadena[:]) ==>asdfsfq;asdsadqw;asdfqwer;asadfqwer

#print(cadena[2:10:2]) ==> dsqa
# print(cadena[-1:-10:-2]) ==> rwfaa


#for i in range(len(cadena)+1):
    #print(cadena[i]) ===> IndexError: string index out of range

#print("as" in cadena) ==> True


#print(type(cadena2))
#print(cadena2)
#print(cadena)

#print(cadena.lstrip()) #quita espacios izquierda
#print(cadena.rstrip()) #quita espacios derecha
#print(cadena.strip()) #quita espacios de los dos lados
#PARA QUITAR ESPACIOS ===> print(cadena.replace(" ",""))
