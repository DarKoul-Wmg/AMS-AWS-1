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
xml = read_xml('../dades/fruites.xml')
tree = etree.XML(xml)

# Obtenir el nom de les fruites en una llista [array]
nomsFruites = tree.xpath('/fruites/*/nom/text()')
print(0, nomsFruites)

# Obtenir el nom de la primera fruita [1]
nomPrimera = tree.xpath('/fruites/fruita[1]/nom/text()')
print(1, nomPrimera)

# Obtenir el nom de fruita amb [@id=1]
nomPrimera = tree.xpath('/fruites/fruita[@id=1]/nom/text()')
print(2, nomPrimera)

# Obtenir el nom de la última fruita [last()]
nomUltima = tree.xpath('/fruites/fruita[last()]/nom/text()')
print(3, nomUltima)

# Obtenir el nom de la penúltima fruita [last()-1]
nomPenultima = tree.xpath('/fruites/fruita[last()-1]/nom/text()')
print(4, nomPenultima)

# Obtenir les tres primeres fruites [position()<=3]
tresPrimeres = tree.xpath('/fruites/fruita[position()<=3]/nom/text()')
print(5, tresPrimeres)

# Obtenir les tres últimes fruites [last()-2<=position()]
tresUltimes = tree.xpath('/fruites/fruita[last()-2<=position()]/nom/text()')
print(6, tresUltimes)

# Obtenir les fruites de color groc [color="groc"]
fruitesGroc = tree.xpath('/fruites/fruita[color="groc"]/nom/text()')
print(7, fruitesGroc)

# Obtenir les fruites que no són de color groc [not]
fruitesNoGroc = tree.xpath('/fruites/fruita[not(color="groc")]/nom/text()')
print(8, fruitesNoGroc)

# Obtenir les fruites que costen 0.5 o menys [<=]
fruites05 = tree.xpath('/fruites/fruita[preu<=0.5]/nom/text()')
print(9, fruites05)

# Obtenir les fruites que comencen per 'p' [starts-with()]
fruitesP = tree.xpath('/fruites/fruita[nom[starts-with(., "p")]]/nom/text()')
print(10, fruitesP)

# Obtenir les fruites que contenen 'a' [contains()]
fruitesA = tree.xpath('/fruites/fruita[nom[contains(., "o")]]/nom/text()')
print(11, fruitesA)

# Obtenir les fruites que són de color groc o taronja [or]
fruitesGrocVermell = tree.xpath('/fruites/fruita[color="groc" or color="taronja"]/nom/text()')
print(12, fruitesGrocVermell)

# Obtenir les fruites que són de color verd i costen més de 0.4 [and]
fruitesGroc05 = tree.xpath('/fruites/fruita[color="verd" and preu>0.4]/nom/text()')
print(13, fruitesGroc05)

# Obtenir el número de fruites [count()]
numFruites = tree.xpath('count(/fruites/fruita)')
print(14, numFruites)

# Obtenir les fruites amb posició parell
fruitesParell = tree.xpath('/fruites/fruita[position() mod 2 = 0]/nom/text()')
print(15, fruitesParell)

# Obtenir les fruites amb id parell
fruitesIdParell = tree.xpath('/fruites/fruita[@id mod 2 = 0]/nom/text()')
print(16, fruitesIdParell)