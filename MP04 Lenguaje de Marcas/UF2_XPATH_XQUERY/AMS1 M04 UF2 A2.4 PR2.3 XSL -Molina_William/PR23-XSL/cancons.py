from lxml import etree
import os

# Llegir un arxiu XML
def read_xml(path):
   file = open(path, 'r', encoding='utf-8')
   string = file.read()
   file.close()
   return bytes(bytearray(string, encoding='utf-8'))


# Escriure un arxiu HTML
def write_html(path, html):
   file = open(path, 'w', encoding='utf-8')
   file.write(html)
   file.close()

# Transformar una canco de XML a HTML
def transform_canco(xmlTree, id):
   # Crear l'arbre XSL per una canco
   xslcanco = read_xml('./xml/template-canco.xsl')
   xslTree = etree.XML(xslcanco)

   # Transformar l'arxiu de dades-cancons.xml segons l'arxiu template-canco.xsl i guardar-lo en un .html
   transform = etree.XSLT(xslTree)
   htmlDom = transform(xmlTree, paramId=id)
   htmlResult = etree.tostring(htmlDom, pretty_print=True).decode('utf-8')
   write_html("./html/cancons/"+id+".html", htmlResult)

# Crear un índex.html amb totes les cancons
def transform_index_cancons(xmlTree):
   # Crear l'arbre XSL per l'index de totes les cancons
   xslcancons = read_xml('./xml/template-cancons.xsl')
   xslTreecancons = etree.XML(xslcancons)

   # Transformar l'arxiu de dades-cancons.xml segons l'arxiu template-cancons.xsl i guardar-lo a index.html
   transform = etree.XSLT(xslTreecancons)
   htmlDom = transform(xmlTree)
   htmlResult = etree.tostring(htmlDom, pretty_print=True).decode('utf-8')
   write_html("./html/cancons/index.html", htmlResult)

# Crear l'arbre XML
xml = read_xml('./xml/dades-cancons.xml')
xmlTree = etree.XML(xml)

# Esborrar els arxius .html creats anteriorment
for file in os.listdir("./html/cancons"):
   if file.endswith(".html"):
      os.remove("./html/cancons/"+file)

# Generar cada una de les cancons a arxius .html
for canco in xmlTree:
   transform_canco(xmlTree, canco.get('id'))

# Generar l'índex de totes les cancons
transform_index_cancons(xmlTree)
