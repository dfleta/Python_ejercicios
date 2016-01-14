
from tablaAsignacion import *

class Dni:
	def __init__(self, cadena = ""):
		self.dni  = cadena
		self.numeroSano = False
		self.letraSana 	= False
		# Composición (agregación) "Has - a" / "Tiene - un"
		self.tabla = TablaAsignacion()

	### interfaz PUBLICA ###

	def setDni(self, cadena):
		self.dni = cadena

	def getDni(self):
		return self.dni

	def setNumeroSano(self, valor):
		self.numeroSano = valor

	def getNumeroSano(self):
		return self.numeroSano

	def setLetraSana(self, valor):
		self.letraSana = valor

	def getLetraSana(self):
		return self.letraSana


	def checkCIF(self):
		return self.checkDni() and self.checkLetra()

	def checkDni(self):
		self.setNumeroSano( self.checkLongitud() and self.checkNumero() )
		return self.getNumeroSano()

	def checkLetra(self):
		if self.getNumeroSano():
			self.setLetraSana ( self.getParteAlfabeticaDni().isupper() and not self.getParteAlfabeticaDni().isdigit() and self.checkLetraValida() )
			return self.getLetraSana()
		else:
			return False

	def obtenerLetra(self):
		# calcularLetra no puede ejecutarse si antes no se cumplen las condiciones previas en checkDni
		# y checkletra
		if self.getNumeroSano():
			return self.tabla.calcularLetra( self.getParteNumericaDni() )
		else:
			return False

	### parte PRIVADA ###

	def checkLongitud(self):
		return len(self.dni) == 9

	def checkNumero(self):
		return self.dni[:-1].isdigit()

	def checkLetraValida(self):
		if self.getNumeroSano():
			return self.getParteAlfabeticaDni() == self.obtenerLetra()
		else:
			return False

	def getParteAlfabeticaDni(self):
		return self.dni[-1]

	def getParteNumericaDni(self):
		if self.getNumeroSano():
			return self.dni[:-1]
		else:
			return False



if __name__ == 	'__main__':

	import math
	import random

	### Casos test ALEATORIOS ###

	casosTest = []
	numeroCasos = 25

	for i in range(1, numeroCasos + 1):
		caso = ""
		for j in range(1, 9):
			# random.randrange(start, stop[, step])
			# numeroAleatorio = random.randint(0, 9)
			# ASCII 48-57 = 0-9    65-90 = A-Z   58 = ":"
			# generamos un numero aleatorio entre 48 y 58 
			caracterAscii = random.randrange(48, 58 + 1, 1)
			# convertimos el numero ASCII a caracter. chr() toma el argumento como codigo ASCII de un caracter
			caso = caso + chr(caracterAscii)
		# en la ultima posicion añado una letra A-Z
		caso = caso + chr(random.randrange(65, 90 + 1, 1) )
		casosTest = casosTest + [caso]

	print(casosTest)

	for dni in casosTest:
		objeto = Dni(dni)
		print(objeto.getDni())
		objeto.checkCIF()
		print('dni --->', objeto.getNumeroSano())
		# print(objeto.calcularLetra())
		print('Letra --->', objeto.getLetraSana())
		print('La letra es', objeto.obtenerLetra() )


	### Casos test OK ###

	casosTest = [ #casos OK
				 "78484464T","72376173A","01817200Q","95882054E","63587725Q",
				 "26861694V","21616083Q","26868974Y","40135330P","89044648X",
				 "80117501Z","34168723S","76857238R","66714505S","66499420A"]

	print("\n #### CASOS OK #### \n")

	for dni in casosTest:
		objeto = Dni(dni)
		print(objeto.getDni())
		objeto.checkCIF()
		print('dni --->', objeto.getNumeroSano())
		# print(objeto.calcularLetra())
		print('Letra --->', objeto.getLetraSana())
		print('La letra es', objeto.obtenerLetra() )
	

