from lxml import etree

def read_xml(path):
    file = open(path, 'r', encoding='utf-8')
    string = file.read()
    file.close()
    return bytes(bytearray(string, encoding='utf-8'))

xml = read_xml('bailes.xml')
tree = etree.XML(xml)

#1 - Muestra el nombre de cada baile que tenga cuota trimestral.
result = tree.xpath('/bailes/baile[precio [@cuota ="trimestral"]]/nombre/text()')
print(1, result)

#2 - Muestra los bailes que puedan aprender despues de la fecha: 2011-04-01.
result = tree.xpath('/bailes/baile[comienzo >"2011-04-01"]/nombre/text()')

#result = tree.xpath('/bailes/baile[xs:date(comienzo) > xs:date("2011-04-01")]/nombre/text()')

print(2, result)

#3 - Muestra los profesores que cobren en "euro".                    Evitar repetición de un profesor
result = tree.xpath('/bailes/baile[precio[@moneda = "euro"]]/profesor[not(. = preceding::profesor)]/text()')
print(3, result)


#4 - Muestra el total de bailes que hay. 
result = tree.xpath('count(/bailes/baile)')
print(4, result)

#5 - Muestra los bailes que tengan cuota que empieza por "3".
result = tree.xpath('/bailes/baile[starts-with(precio,"3")]/nombre/text()')
print(5, result)


