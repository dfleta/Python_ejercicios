
# capa de acceso a datos

class AccesoDatos:

	def __init__(self, repositorio):	
		# patron Fachada: en funcion del tipo de repositorio, configura las variables que
		# definen la interfaz con los datos con las funciones adecuadas
		self.__repositorio  	= repositorio
		self.__leerDatos  		= None		# devolvera una lista de tuplas = argumentos de persona
		self.__escribirDatos 	= None		
		self.__borrarDatos 		= None
		
		self.tipoRepositorio()			
		# en __leerDatos tendremos los datos en forma de lista de tuplas al iniciar el objeto 

	def getDatos(self):
		return self.__leerDatos

	datos = property(getDatos)

	def tipoRepositorio(self):
		# logica que devuelve el metodo de lectura adecuado a cada tipo de repositorio
		if isinstance(self.__repositorio, dict):
			self.__preparar_diccionario()

		elif self.__repositorio.endswith(".txt"):
			self.__preparar_TXT()

		else: pass # conexion a redis

	def __preparar_diccionario(self):
		# configura __leerDatos con la funcion que extrae los datos de un diccionario
		def leerDiccionario():
			diccionario = self.__repositorio	
			return [ (item,) + tuple( diccionario[item].values() ) for item in diccionario ]
		self.__leerDatos = leerDiccionario()

				
	def __preparar_TXT(self):
		def leerTXT():
			listaRegistros = [ linea.rstrip().split() for linea in open(self.__repositorio) ]
			listaRegistrosConvertida = [  tuple( int(item) if item.isdigit() else item for item in lista )  for lista in listaRegistros  ][1:]
			return listaRegistrosConvertida 	# devolver una lista de tuplas 
		self.__leerDatos = leerTXT()
				

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
			'''
			Python can do better than prototyping: instead of needing to clone an existing 
			object and modify the clone, Python gives us access to any object’s class object, 
			so that we can create a new object directly and much more efficiently than by cloning.
			'''

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

	datos = AccesoDatos(data)

	personal = Plantilla(datos, Persona)

	personal.crearPlantilla()

	personal.mostrarPlantilla()

	print(personal)


	# origen datos fichero txt

	data = "data_prototipo.txt"

	datos = AccesoDatos(data)

	personal = Plantilla(datos, Persona)

	personal.crearPlantilla()

	personal.mostrarPlantilla()

	print(personal)
