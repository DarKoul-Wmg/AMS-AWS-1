from lxml import etree


def read_xml(path):
    file = open(path, 'r', encoding='utf-8')
    string = file.read()
    file.close()
    return bytes(bytearray(string, encoding='utf-8'))

xml = read_xml('books.xml')
tree = etree.XML(xml)

# Muestra el título de cada libro cuyo precio sea mayor o igual a 30.
result = tree.xpath('/bookstore/book[price >= 30]/title/text()')
print(1, result)

# Muestra los autores de cada libro donde la fecha de publicacion sea el 2005, sin repetir. 
result = tree.xpath('/bookstore/book[year = 2005]/author[not(. = preceding::author)]/text()') # en este caso no es necesario
print(2, result)

# Muestra los años de publicación sin repetir. 
result = tree.xpath('/bookstore/book/year[not(. = preceding::year)]/text()')
print(3, result)

# Muestra el total de libros que hay. 
result = tree.xpath('count(/bookstore/book)')
print(4, result)

# Muestra el titulo de los libros escritos en años que terminen en "3". 
result = tree.xpath('/bookstore/book[ends-with(year,"3")]/title/text()')
print(5, result)


