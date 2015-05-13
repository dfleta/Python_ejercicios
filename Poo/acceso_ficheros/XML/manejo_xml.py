
#https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

# ElementTree represents the whole XML document as a tree, 
# and Element represents a single node in this tree. 
# Interactions with the whole document (reading and writing to/from files)
# are usually done on the ElementTree level. 
# Interactions with a single XML element and its sub-elements are done on the Element level.

import xml.etree.ElementTree as ET

tree = ET.parse('data_prototipo.xml')

print(type(tree))

root = tree.getroot()

print(root.tag)

# It also has children nodes over which we can iterate:

for child in root:
	print(child.tag, child.attrib)

# Element.findall() finds only elements with a tag which are direct children of the current element.
# Element.find() finds the first child with a particular tag, 
# and Element.text accesses the element s text content. 
# Element.get() accesses the element s attributes:


for child in root.iter('nombre'):
	print(child.tag + ' = ' + child.text)

for persona in root.findall('persona'):
	nombre = persona.find('nombre').text
	horas = persona.find('horas').text
	print(nombre, horas)

print([ (persona.find('nombre').text, persona.find('horas').text, persona.find('rate').text) 
				for persona in root.findall('persona') ] )


