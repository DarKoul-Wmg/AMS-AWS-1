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

# Crear un índex.html amb les 5 primeres noticies
def transform(xmlTree, type):
   # Crear l'arbre XSL per l'index de totes les noticies
   xslmicro = read_xml('./xml/template-microsiervos.xsl')
   xslTreemicro = etree.XML(xslmicro)
   # Transformar l'arxiu de dades-microsiervos.rss segons l'arxiu template-microsiervos.xsl
   transform = etree.XSLT(xslTreemicro)
   htmlDom = transform(xmlTree, paramType="'" + type + "'")
   htmlResult = etree.tostring(htmlDom, pretty_print=True).decode('utf-8')
   write_html("./html/microsiervos/microsiervos-"+type+".html", htmlResult)

# Crear l'arbre XML
xml = read_xml('./xml/dades-microsiervos.rss')
xmlTree = etree.XML(xml)

# Generar l'arxiu de les 5 primeres noticies
transform(xmlTree, "5")

transform(xmlTree, "Espai")

transform(xmlTree, "Imparell")