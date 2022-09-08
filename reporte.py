
import xml.etree.cElementTree as ET
import os

ruta=os.path.dirname(os.path.abspath(__file__))
ruta = ruta + "/"
print(ruta)
root = ET.Element("pacientes")

i = 0
for numero in range(1,10):
    doc = ET.SubElement(root, "paciente")
    ET.SubElement(doc, "nodo1", name="nodo").text="Texto nod01"
    ET.SubElement(doc, "nodo2", name="nodo").text="Texto nod02"
    ET.SubElement(doc, "nodo3", name="nodo").text="Texto nod03"
    i += 1

archivo = ET.ElementTree(root)
archivo.write(ruta + "ejemplo.xml")