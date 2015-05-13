
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
			parteNumericaDni = int( self.getParteNumericaDni() )
			posicion = parteNumericaDni % 23
			return self.tabla.getLetra(posicion)
		else: 
			return False
	



if __name__ == 	'__main__':

	cadenas = [ '44453296T', '53179805X', '12345678O', 'A2345678X', '44453296X']

	for dni in cadenas:
		objeto = Dni(dni)
		print(objeto.getDni())
		objeto.checkDni()
		print(objeto.getSano())
		print(objeto.obtenerLetra())
		print('La letra es', objeto.obtenerLetra() )

		# objeto.printTabla()
		# objeto.mostrarTabla() => Como no hay herencia, no funciona


	

