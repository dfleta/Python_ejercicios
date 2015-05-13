
class Dni():
	def __init__(self, cadena = ""):
		self.dni  = cadena
		self.sano = False

	def setDni(self, cadena):
		self.dni = cadena

	def getDni(self):
		return self.dni

	def setSano(self, valor):
		self.sano = valor

	def getSano(self):
		return self.sano

	def checkDni(self):
		if self.checkLongitud() and self.checkNumero() and self.checkLetra():
			self.setSano(True)

	def checkLongitud(self):
		return len(self.dni) == 9

	def checkNumero(self):
		return self.dni[:-1].isdigit()

	def checkLetra(self):
		return self.dni[-1].isupper() and not self.dni[-1].isdigit()

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
	

