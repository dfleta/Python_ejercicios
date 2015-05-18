
from abc import ABCMeta, abstractmethod

import json
import xml.etree.ElementTree as ET

# capa de acceso a datos

## clase abstracta que provee del punto de extension para aplicar Open Close Principle

class AccesoDatos:

	def __init__(self, repositorio):
		# patron Fachada: en funcion del tipo de repositorio, configura las variables que
		# definen la interfaz con los datos con las funciones adecuadas
		self.repositorio  		= repositorio
		self.leerDatos  		= None		# devolvera una lista de tuplas = argumentos de persona
		self.escribirDatos 		= None		
		self.borrarDatos 		= None
		
		self.preparar()			
		# En leerDatos colocaremos los datos en forma de lista de tuplas (argumentos posicionales) para iniciar el objeto
		# El metodo preparar() seria el Draw() de la public interface Shape del ejemplo 
		# Listing 9-2. OOD solution to Square/Circle problem libro Agile Principles Patterns and Practices de Martin.

	def getDatos(self):
		return self.leerDatos

	datos = property(getDatos)

	@abstractmethod	
	def preparar(self):
		pass


# Las clases que heredan de AccesoDatos solo han de implementar el metodo preparar().
# Para extender el comportamiento del programa para que acceda a una nueva fuente de datos
# no es necesario modificar el codigo, solo crear una nueva clase. 
# El codigo resulta mucho mas legible.

class Diccionario(AccesoDatos):

	def preparar(self):
		# configura leerDatos con la funcion que extrae los datos de un diccionario
		def leerDiccionario():
			diccionario = self.repositorio	
			return [ (item,) + tuple( diccionario[item].values() ) for item in diccionario ]
		self.leerDatos = leerDiccionario()


class JSON(AccesoDatos):

	def preparar(self):
		def leerJSON():
			diccionario = json.load( open(self.repositorio) )
			return [ (item,) + tuple( diccionario[item].values() ) for item in diccionario ]
		self.leerDatos = leerJSON()


class XML(AccesoDatos):

	def preparar(self):
		def leerXML():
			arbol = ET.parse(self.repositorio)
			root = arbol.getroot()
			return [ ( persona.find('nombre').text, persona.find('horas').text, persona.find('rate').text ) 
				for persona in root.findall('persona') ]
		self.leerDatos = leerXML()		


class TXT(AccesoDatos):

	def preparar(self):
		def leerTXT():
			listaRegistros = [ linea.rstrip().split() for linea in open(self.repositorio) ]
			listaRegistrosConvertida = [  tuple( int(item) if item.isdigit() else item for item in lista )  for lista in listaRegistros  ][1:]
			return listaRegistrosConvertida 	# devolver una lista de tuplas 
		self.leerDatos = leerTXT()
				

# capa de logica

class Persona:

	def __init__(self, name = "proto", hours = 0 , rate = 0):
		self.__name = name
		self.__hours = hours
		self.__rate = rate

	def __repr__(self):
		return "%s %d" % (self.__name, self.__hours)

	def getName(self):
		return self.__name
	def setName(self, value):
		self.__name = value
	# atributo de clase
	name = property(getName, setName)

	def pay(self):
		return self.hours * self.rate


class Plantilla:
	# composicion de objetos Persona
	def __init__(self, datos, Componente):
		self.plantilla = []
		self.__datos   = datos
		self.__Componente = Componente

	def __repr__(self):
		# comprension
		return "%s" % [item.name for item in self.plantilla]

	def crearPlantilla(self): # patron prototipo
		
		coleccionPargs = datos.datos 	# datos.getDatos()
		# SOLID => abstraccion: cargar datos = interfaz abstracta = capa acceso a datos
		
		prototipo = self.__Componente() 
		# creamos el prototipo. No es necesario: solo para hacerlo explicito =>
		
		for item in coleccionPargs: 
			self.plantilla.append(	prototipo.__class__( *item ) )
			# => self.plantilla.append(	self.__Componente.__class__( *item ) )

	def mostrarPlantilla(self):
		for item in self.plantilla: 
		# SOLID => abstraccion: mostrar datos = interfaz abstracta: no depende de la estructura
			print(item.name)
			

if __name__ == '__main__':

	# origen datos diccionario

	data = {'John': 
					{'horas': 2,
					 'rate': 25},
			'Paul': 
					{'horas': 2,
					 'rate': 25},
			'Ringo': 
					{'horas': 2,
					 'rate': 5},
			'George': 
					{'horas': 2,
					 'rate': 15},
			}

	datos = Diccionario(data)

	personal = Plantilla(datos, Persona)

	personal.crearPlantilla()

	personal.mostrarPlantilla()

	print(personal)

	# origen datos fichero JSON

	# https://docs.python.org/3/library/json.html


	data = "data_prototipo.json"

	datos = JSON(data)

	personal = Plantilla(datos, Persona)

	personal.crearPlantilla()

	personal.mostrarPlantilla()

	print(personal)


	# origen datos fichero XML


	data = "data_prototipo.xml"

	datos = XML(data)

	personal = Plantilla(datos, Persona)

	personal.crearPlantilla()

	personal.mostrarPlantilla()

	print(personal)

	# origen datos fichero txt

	data = "data_prototipo.txt"

	datos = TXT(data)

	personal = Plantilla(datos, Persona)

	personal.crearPlantilla()

	personal.mostrarPlantilla()

	print(personal)
