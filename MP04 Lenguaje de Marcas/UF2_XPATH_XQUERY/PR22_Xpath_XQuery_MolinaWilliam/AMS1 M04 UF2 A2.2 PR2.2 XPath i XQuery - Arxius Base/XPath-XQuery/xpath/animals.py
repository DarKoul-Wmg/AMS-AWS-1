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
xml = read_xml('../dades/animals.xml')
tree = etree.XML(xml)

# Obtenir la llista de les espècies animals
especies = tree.xpath('../especies_animals/especie/nom/text()')
print(0, especies)

# Obtenir la llista de les espècies que tenen una 'a' al nom
especiesA = tree.xpath('../especies_animals/especie[contains(nom, "a")]/nom/text()')
print(1, especiesA)

# Obtenir les dues primeres espècies de la llista
duesPrimeres = tree.xpath('../especies_animals/especie[position() <= 2]/nom/text()')
print(2, duesPrimeres)

# Obtenir les dues últimes espècies de la llista
duesUltimes = tree.xpath('../especies_animals/especie[position() > last() -2]/nom/text()')
print(3, duesUltimes)

# Obtenir les espècies que comencen per 'p'
especiesP = tree.xpath('../especies_animals/especie[starts-with(nom,"p")]/nom/text()')
print(4, especiesP)

# Obtenir el segon animal de l'especie amb [@id=2]
animal2 = tree.xpath('../especies_animals/especie[@id = 2]/animals/animal[2]/nom/text()')
print(5, animal2)

# Obtenir el primer animal de l'especie amb [@id=3]
animal3 = tree.xpath('../especies_animals/especie[@id = 3]/animals/animal[1]/nom/text()')
print(6, animal3)

# Obtenir l'últim animal dels ocells
ultimOcell = tree.xpath('../especies_animals/especie[nom = "ocells"]/animals/animal[last()]/nom/text()')
print(7, ultimOcell)

# Obtenir els dos últims peixos
dosUltimsPeixos = tree.xpath('../especies_animals/especie[nom = "peixos"]/animals/animal[position() > last() - 2]/nom/text()')
print(8, dosUltimsPeixos)

# Obtenir els tres primers animals mamífers
tresPrimersMamifers = tree.xpath('../especies_animals/especie[nom = "mamífers"]/animals/animal[position() <= 3]/nom/text()')
print(9, tresPrimersMamifers)

# Obtenir els dos últims ocells
dosUltimsOcells = tree.xpath('../especies_animals/especie[nom = "ocells"]/animals/animal[position() > last() - 2]/nom/text()')
print(10, dosUltimsOcells)

# Obtenir els peixos que pesen menys de 500
peixosMenys500 = tree.xpath('../especies_animals/especie[nom = "peixos"]/animals/animal[pes < 500]/nom/text()')
print(11, peixosMenys500)

# Obtenir els crustacis que pesen 0.5
crustacis05 = tree.xpath('../especies_animals/especie[nom = "crustacis"]/animals/animal[pes = 0.5]/nom/text()')
print(12, crustacis05)

# Obtenir els mamífers que pesen entre 100 i 1000 (incluits)
mamifers1001000 = tree.xpath('../especies_animals/especie[nom = "mamífers"]/animals/animal[pes <= 1000 and pes >= 100]/nom/text()')
print(13, mamifers1001000)

# Obtenir els animals de color gris
animalsBlau = tree.xpath('../especies_animals/especie/animals/animal[color = "gris"]/nom/text()')
print(14, animalsBlau)

# Obtenir els animals que tenen una o al nom
animalsO = tree.xpath('../especies_animals/especie/animals/animal[contains(nom,"o")]/nom/text()')
print(15, animalsO)

# Obtenir els peixos amb id entre 1 i 4 incluits
peixos14 = tree.xpath('../especies_animals/especie[nom = "peixos"]/animals/animal[@id >= 1 and @id <=4]/nom/text()')
print(16, peixos14)

# Obtenir els animals que no són de color gris ni de color vermell
animalsNoVermell = tree.xpath('../especies_animals/especie/animals/animal[color != "gris" and color != "vermell"]/nom/text()')
print(17, animalsNoVermell)

# Obtenir els animals que no son crustacis ni peixos
animalsNoCrustacisPeixos = tree.xpath('../especies_animals/especie[nom != "crustacis" and nom != "peixos"]/animals/animal/nom/text()')
print(18, animalsNoCrustacisPeixos)

# Obtenir els animals que no son crustacis ni peixos i que tenen una l al nom
animalsNoCrustacisPeixosL = tree.xpath('../especies_animals/especie[nom != "crustacis" and nom != "peixos"]/animals/animal[contains(nom,"l")]/nom/text()')
print(19, animalsNoCrustacisPeixosL)

