
# ejemplo Principio de Inversion de Dependencias de SOLID
# libro Agile Principles, Patterns and Practices in C#
# ejemplo furnace pag. 209

from abc import ABCMeta, abstractmethod


# clases abstractas (metaclases) que componen el sistema de calefaccion

class Calefaccion(metaclass = ABCMeta):

	def __init__(self):
		self.combustible = None 

	@abstractmethod
	def encender(self):
		pass

	@abstractmethod
	def apagar(self):
		pass

	@abstractmethod
	def cargarCombustible(self, unidades):
		pass

	@abstractmethod
	def quemarCombustible(self): 	
		pass
	# si hacemos este metodo privado __quemarCombustible =>
	# => en las clases heredadas no podemos acceder a el llamandolo __quemarCombustible,
	# ya que sustituye el nombre por _Calefaccion__quemarCombustible

class Sensor(metaclass = ABCMeta):

	@abstractmethod
	def leer(self): 
		pass


# sistema de calefaccion = calefaccion + sensor

class SistemaCalefaccion():

	# el sistema de calefaccion es la unidad mas alta de logica:
	# no debe depender de la implementacion de calefaccion y sensor

	def __init__(self, calefaccion, sensor):
		self.__calefaccion  = calefaccion
		self.__sensor 		= sensor
		self.temperaturaObjetivo = None

	def on(self, temperaturaObjetivo):

		# esta seria la interfaz "Regulate" del ejemplo

		self.temperaturaObjetivo = temperaturaObjetivo
		
		while ( self.__sensor.leer() < self.temperaturaObjetivo ) & ( self.__calefaccion.combustible > 0 ):
			self.__calefaccion.encender()
			print('quedan :', self.__calefaccion.combustible)

		self.off()


	def off(self):
		self.__calefaccion.apagar()



# Implementaciones de Calefaccion

class Chimenea(Calefaccion):

	# es necesario definir todos los metodos abstractos de la metaclase
	# sino, no podremos instanciar esta clase

	def encender(self):
		self.quemarCombustible()
		print('Dando calorcito y quemando leña')

	def apagar(self):
		print('Apagando la chimenea')

	def cargarCombustible(self, unidades):
		self.combustible = unidades

	def quemarCombustible(self):
		self.combustible -= 1


class SueloRadiante(Calefaccion):
	
	def encender(self):
		self.quemarCombustible()
		print('Quemando gas!')

	def apagar(self):
		print('Apagando el suelo radiante')

	def cargarCombustible(self, unidades):
		self.combustible = unidades

	def quemarCombustible(self):
		self.combustible -= 2 		# el suelo radiante consume mas :(

# Implementaciones de Sensor


class Termometro(Sensor):
	def leer(self):
		return 10


class Termostato(Sensor):
	def leer(self):
		return 10


##########################3 main

# chimenea = Calefaccion() => no es posible instanciar clase con metodos abstractos

# termo = Sensor() => no es posible instanciar clase con metodos abstractos


# implementacion con chimenea y termostato

chimenea = Chimenea()
# chimenea.encender()

termo = Termostato()
print(termo.leer())

sistema = SistemaCalefaccion(chimenea, termo)

chimenea.cargarCombustible(4)
sistema.on(24)


# implementacion con suelo radiante y termometro

suelo = SueloRadiante()
# suelo.encender()

termo = Termometro()
print(termo.leer())

sistema = SistemaCalefaccion(suelo, termo)

suelo.cargarCombustible(6)
sistema.on(24)