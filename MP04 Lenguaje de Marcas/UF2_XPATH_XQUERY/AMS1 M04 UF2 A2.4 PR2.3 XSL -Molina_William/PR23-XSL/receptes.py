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

# Transformar una recepta de XML a HTML
def transform_recepta(xmlTree, id):
   # Crear l'arbre XSL per una recepta
   xslRecepta = read_xml('./xml/template-recepta.xsl')
   xslTree = etree.XML(xslRecepta)

   # Transformar l'arxiu de dades-receptes.xml segons l'arxiu template-recepta.xsl i guardar-lo en un .html
   transform = etree.XSLT(xslTree)
   htmlDom = transform(xmlTree, paramId=id)
   htmlResult = etree.tostring(htmlDom, pretty_print=True).decode('utf-8')
   write_html("./html/receptes/"+id+".html", htmlResult)

# Crear un índex.html amb totes les receptes
def transform_index_receptes(xmlTree):
   # Crear l'arbre XSL per l'index de totes les receptes
   xslReceptes = read_xml('./xml/template-receptes.xsl')
   xslTreeReceptes = etree.XML(xslReceptes)

   # Transformar l'arxiu de dades-receptes.xml segons l'arxiu template-receptes.xsl i guardar-lo a index.html
   transform = etree.XSLT(xslTreeReceptes)
   htmlDom = transform(xmlTree)
   htmlResult = etree.tostring(htmlDom, pretty_print=True).decode('utf-8')
   write_html("./html/receptes/index.html", htmlResult)

# Crear l'arbre XML
xml = read_xml('./xml/dades-receptes.xml')
xmlTree = etree.XML(xml)

# Esborrar els arxius .html creats anteriorment
for file in os.listdir("./html/receptes"):
   if file.endswith(".html"):
      os.remove("./html/receptes/"+file)

# Generar cada una de les receptes a arxius .html
for recepta in xmlTree:
   transform_recepta(xmlTree, recepta.get('id'))

# Generar l'índex de totes les receptes
transform_index_receptes(xmlTree)
