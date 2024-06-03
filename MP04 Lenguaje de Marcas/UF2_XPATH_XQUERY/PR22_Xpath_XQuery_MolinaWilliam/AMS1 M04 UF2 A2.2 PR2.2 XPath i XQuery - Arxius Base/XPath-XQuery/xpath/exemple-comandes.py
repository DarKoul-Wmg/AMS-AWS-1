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
xml = read_xml('../dades/comandes.xml')
tree = etree.XML(xml)

# Obteinr el nom del segon producte [2]
nomSegona = tree.xpath('/comanda/producte[2]/nom/text()')
print(0, nomSegona)

# Obtenir el nom de les comandes en una llista [array]
nomsComandes = tree.xpath('/comanda/*/nom/text()')
print(0, nomsComandes)

# Obtenir l'artibut 'codi' del primer producte
codiPrimera = tree.xpath('/comanda/producte[1]/@codi')
print(1, codiPrimera)

# Obtenir l'artibut 'codi' del primer producte
codiPrimera = tree.xpath('/comanda/producte[ancestor::comanda]/@codi')
print(1, codiPrimera) # Retorna ['a0', 'a1']

# Obtenir els fills anteriors al segon producte
fillsAnteriors = tree.xpath('/comanda/producte[2]/preceding::*/nom/text()')
print(2, fillsAnteriors) # Retorna ['Xinxeta']