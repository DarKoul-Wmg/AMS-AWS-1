#a
fichero = open("16arxiu","w+")
content = "All paid jobs absorb and degrade the mind.\n " \
          "If Beethoven had been killed in a plane crash at the age of 22, it would have changed\n " \
          "the history of music... and of aviation.\n " \
          "I do not have a psychiatrist and I do not want one, for the simple reason that if he\n" \
          "listened to me long enough, he might become disturbed."
fichero.write(content)

#b
fichero.seek(0)
print(fichero.readline())

#c
cont = 0
while True:
    fichero.seek(cont,0) #dede inicio
    if fichero.read(4) == "mind":
        print("Posición mind: "+ str(fichero.tell()))
        break
    else:
        cont +=1

#e
print("no e")

#g
fichero.seek(0, 2)


end_position = fichero.tell()

position = end_position - 1
fichero.seek(position)


while position >= 0:
    char = fichero.read(1)
    if char == '\n':
        break
    position -= 1
    fichero.seek(position)

#última línea
last_line = fichero.readline()
print(last_line)





