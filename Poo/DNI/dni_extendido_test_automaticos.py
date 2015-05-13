
from tablaAsignacion import *


class Dni:
	def __init__(self, cadena = ""):
		self.dni  = cadena
		self.sano = False
		# Composición (agregación) "Has - a" / "Tiene - un"
		self.tabla = TablaAsignacion()

	# interfaz publicaº
	# parte privada

	def setDni(self, cadena):
		self.dni = cadena

	def getDni(self):
		return self.dni

	def setSano(self, valor):
		self.sano = valor

	def getSano(self):
		return self.sano

	def letraCorrecta(self, letra):
		return self.tabla.letraPermitida(letra)


	def printTabla(self):
		self.tabla.mostrarTabla()

	def getParteNumericaDni(self):
		if self.getSano():
			return self.dni[:-1]
		else:
			return False

	def checkDni(self):
		if self.checkLongitud() and self.checkNumero() and self.checkLetra():
			self.setSano(True)
		else: 
			self.setSano(False)

	def checkLongitud(self):
		return len(self.dni) == 9

	def checkNumero(self):
		return self.dni[:-1].isdigit()

	def checkLetra(self):
		return self.dni[-1].isupper() and not self.dni[-1].isdigit() and self.letraCorrecta(self.dni[-1])

	def obtenerLetra(self):
		# obtener el numero del dni del string => dni sano
		# dividirlo por 23, obtener el resto
		# consultar TablaAsignacion con ese resto = posicion

		self.checkDni()

		if self.getSano():
			posicion = int( self.getParteNumericaDni() ) % self.tabla.getModulo()
			return self.tabla.getLetra(posicion)
		else: 
			return False
	



if __name__ == 	'__main__':

	import math
	import random

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
		# en la ultima posicion anhado una letra A-Z
		caso = caso + chr(random.randrange(65, 90 + 1, 1) )
		casosTest = casosTest + [caso]

	print(casosTest)

	for dni in casosTest:
		objeto = Dni(dni)
		print(objeto.getDni())
		objeto.checkDni()
		print('Dni sano: ', objeto.getSano())
		print('La letra es', objeto.obtenerLetra() )

		# objeto.printTabla()
		# objeto.mostrarTabla() => Como no hay herencia, no funciona


	

