import xml.dom.minidom
import xml.sax

# Usando o processador DOM para obter nomes de autores
dom_tree = xml.dom.minidom.parse("data/cf79.xml")
autores = dom_tree.getElementsByTagName("AUTHOR")

with open("autores.xml", "w") as f:
    for autor in autores:
        f.write(autor.firstChild.nodeValue.strip() + "\n")

# Usando o processador SAX para obter nomes de títulos
class TitleHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.titulos = []
        self.current_data = ""
 
    def startElement(self, tag, attributes):
        self.current_data = tag
 
    def endElement(self, tag):
        self.current_data = ""
 
    def characters(self, content):
        if self.current_data == "TITLE":
            self.titulos.append(content.strip())
 
parser = xml.sax.make_parser()
handler = TitleHandler()
parser.setContentHandler(handler)
parser.parse("data/cf79.xml")

with open("titulos.xml", "w") as f:
    for titulo in handler.titulos:
        f.write(titulo + "\n")
