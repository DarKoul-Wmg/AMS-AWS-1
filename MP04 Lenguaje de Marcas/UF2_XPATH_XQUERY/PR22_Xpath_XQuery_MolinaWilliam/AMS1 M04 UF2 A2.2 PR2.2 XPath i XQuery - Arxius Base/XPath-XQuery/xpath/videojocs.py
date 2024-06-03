from lxml import etree

# Cal instal·lar:
# pip install lxml 
# python3 -m pip install lxml

# Llegir l'arxiu XML
def read_xml(path):
    file = open(path, 'r', encoding='utf-8')
    string = file.read()
    file.close()
    return bytes(bytearray(string, encoding='utf-8'))

# Crear l'arbre XML
xml = read_xml('../dades/videojocs.xml')
tree = etree.XML(xml)

# Obtenir el nom de les videoconsoles
nomsVideoconsoles = tree.xpath('../consoles/consola/nom/text()')
print(0, nomsVideoconsoles)

# Obtenir els diferents fabricants de consoles
fabricants = tree.xpath('../consoles/consola/fabricant/text()')
fabricantsSenseDuplicats = list(dict.fromkeys(fabricants))
print(1, list(dict.fromkeys(fabricantsSenseDuplicats)))

# Obtenir el nom de les consoles de Sony
nomsSony = tree.xpath('../consoles/consola[fabricant ="Sony"]/nom/text()')
print(2, nomsSony)

# Obtenir el nom de les consoles de Nintendo
nomsNintendo = tree.xpath('../consoles/consola[fabricant ="Nintendo"]/nom/text()')
print(3, nomsNintendo)

# Obtenir les consoles que valen menys de 250
consolesMenys250 = tree.xpath('../consoles/consola[preu < 250]/nom/text()')
print(4, consolesMenys250)

# Obtenir els videojocs que començen per 'G'
videojocsG = tree.xpath('../consoles/consola/videojocs/videojoc[starts-with(nom,"G")]/nom/text()')
print(5, videojocsG)

# Obtenir els videojocs que tenen la paraula 'Mario'
videojocsMario = tree.xpath('../consoles/consola/videojocs/videojoc[contains(nom,"Mario")]/nom/text()')
print(6, videojocsMario)

# Obtenir els videojocs que no són per consoles de Nintendo ni de Sony
videojocsNoNintendoNoSony = tree.xpath('../consoles/consola[fabricant != "Nintendo" and fabricant != "Sony"]/videojocs/videojoc/nom/text()')
print(7, videojocsNoNintendoNoSony)

# Obtenir els videojocs que el desenvolupador conté 'Ubisoft'
videojocsUbisoft = tree.xpath('../consoles/consola/videojocs/videojoc[contains(desenvolupador,"Ubisoft")]/nom/text()')
print(8, videojocsUbisoft)

# Obtenir els videojocs que el desenvolupador conté 'Ubisoft' i el preu és menor de 60
videojocsUbisoftPreuMenor50 = tree.xpath(
    '../consoles/consola/videojocs/videojoc[contains(desenvolupador,"Ubisoft") and preu < 60]/nom/text()')
print(9, videojocsUbisoftPreuMenor50)

# Obtenir els videojocs que valen més o igual 65
videojocsPreuMajor65 = tree.xpath('../consoles/consola/videojocs/videojoc[preu >= 65]/nom/text()')
print(10, videojocsPreuMajor65)

# Obtenir els videojocs amb fabricant Nintendo i desenvolupador diferent de Nintendo
videojocsNintendoNoNintendo = tree.xpath(
    '../consoles/consola[fabricant = "Nintendo"]/videojocs/videojoc[desenvolupador != "Nintendo"]/nom/text()')
print(11, videojocsNintendoNoNintendo)

# Obtenir els tres primers videojocs de Playstation 3
videojocsPS3 = tree.xpath('../consoles/consola[nom = "Playstation 3"]/videojocs/videojoc[position() <= 3]/nom/text()')
print(12, videojocsPS3)

# Obtenir els dos últims videojocs de Xbox One
videojocsXboxOne = tree.xpath('../consoles/consola[nom = "Xbox One"]/videojocs/videojoc[position() > last()-2]/nom/text()')
print(13, videojocsXboxOne)

# Obtenir els videojocs de Xbox One que valen menys de 65
videojocsXboxOnePreuMenor65 = tree.xpath('../consoles/consola[nom = "Xbox One"]/videojocs/videojoc[preu < 65]/nom/text()')
print(14, videojocsXboxOnePreuMenor65)

# Obtenir els videojocs de Xbox One que tenen la lletra 'd' minúscula
videojocsXboxOneLletraD = tree.xpath('../consoles/consola[nom = "Xbox One"]/videojocs/videojoc[contains(nom,"d")]/nom/text()')
print(15, videojocsXboxOneLletraD)

# Obtenir els videojocs de Xbox One que tenen la lletra 'M' majúscula
videojocsXboxOneLletraM = tree.xpath('../consoles/consola[nom = "Xbox One"]/videojocs/videojoc[contains(nom,"M")]/nom/text()')
print(16, videojocsXboxOneLletraM)

# Obtenir els videjocs de Xbox One que tenen la lletra 'M' majúscucla o la 'D' majúscula
videojocsXboxOneLletraMD = \
    tree.xpath('../consoles/consola[nom = "Xbox One"]/videojocs/videojoc[contains(nom,"M") or contains(nom, "D")]/nom/text()')
print(17, videojocsXboxOneLletraMD)

# Obtenir els videojocs de XBox One que tenen la lletra 'M' majúscula i cap 'l' minúsucula
videojocsXboxOneLletraMNoL = \
    tree.xpath('../consoles/consola[nom = "Xbox One"]/videojocs/videojoc[contains(nom,"M") and not (contains(nom, "l"))]/nom/text()')
print(18, videojocsXboxOneLletraMNoL)

# Obtenir els videojocs que valen 65
videojocs65 = tree.xpath('../consoles/consola/videojocs/videojoc[preu = 65]/nom/text()')
print(19, videojocs65)

# Obtenir els videojocs amb fabricant Sony o Microsoft que valen 65
videojocsSonyMicrosoft65 = tree.xpath('../consoles/consola[fabricant = "Sony" or fabricant = "Microsoft"]/videojocs/videojoc[preu = 65]/nom/text()')
print(20, videojocsSonyMicrosoft65)

# Obtenir els videojocs que tenen les paraules 'Galaxy', 'World' o 'Planet'
videojocsGalaxyWorldPlanet = \
    tree.xpath('../consoles/consola/videojocs/videojoc[contains(nom,"Galaxy") or contains(nom,"World") or contains(nom,"Planet")]/nom/text()')
print(21, videojocsGalaxyWorldPlanet)

# Obtenir els videjocs amb id parell i que el nom conté 'Mario'
videojocsIdParellLletraE = tree.xpath('../consoles/consola/videojocs/videojoc[@id mod 2 = 0 and contains(nom,"Mario")]/nom/text()')
print(22, videojocsIdParellLletraE)

# Obtenir els preus de tots els videojocs amb desevolupador 'Ubisoft'
preusUbisoft = tree.xpath('../consoles/consola/videojocs/videojoc[contains(desenvolupador,"Ubisoft")]/preu/text()')
print(23, preusUbisoft)

# Obtenir les consoles de color blanc
consolesBlanc = tree.xpath('../consoles/consola[color = "blanc"]/nom/text()')
print(24, consolesBlanc)

# Ordenar les videoconsoles de Nintendo per preu
consolesNintendo = tree.xpath('../consoles/consola[fabricant = "Nintendo"]/nom/text()')
consolesNintendoOrdenades = sorted(consolesNintendo)
print(25, consolesNintendoOrdenades)
