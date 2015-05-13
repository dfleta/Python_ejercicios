
class TablaAsignacion:

	# podemos utilizar este ejercicio para sobrecarga de operaciones sobre listas
	def __init__(self):
		self.tabla = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 
						'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]

	def getLetra(self, posicion):
		return self.tabla[posicion]

	def letraPermitida(self, letra):
		return letra in self.tabla

	def mostrarTabla(self):
		print(self.tabla)


class Dni:
	def __init__(self, cadena = ""):
		self.dni  = cadena
		self.sano = False
		# Composición (agregación) "Has - a" / "Tiene - un"
		self.tabla = TablaAsignacion()

	# interfaz publica

	def setDni(self, cadena):
		self.dni = cadena

	def getDni(self):
		return self.dni

	def setSano(self, valor):
		self.sano = valor

	def getSano(self):
		return self.sano

	# esta accion no puede invocarse desde esta clase
	def printTabla(self):
		self.tabla.mostrarTabla()

	def checkDni(self):
		if self.checkLongitud() and self.checkNumero() and self.checkLetra():
			self.setSano(True)
		else: 
			self.setSano(False)

	def obtenerLetra(self):
		if self.getSano():
			return self.calcularLetra()
		else:
			return False


	# parte privada

	def letraValida(self, letra):
		return self.tabla.letraPermitida(letra)

	def getParteAlfabetica(self):
		if self.getSano():
			return self.dni[-1]
		else:
			return False	

	def checkLongitud(self):
		return len(self.dni) == 9

	def checkNumero(self):
		return self.dni[:-1].isdigit()

	def checkLetra(self):
		return ( self.dni[-1].isupper() and not self.dni[-1].isdigit() and self.letraValida(self.dni[-1]) 
				and self.dni[-1] == self.calcularLetra() )

	def calcularLetra(self):
		# obtener el numero del dni del string => dni sano
		# dividirlo por 23, obtener el resto
		# consultar TablaAsignacion con ese resto = posicion

		# calcularLetra no puede ejecutarse si antes no se cumplen las condiciones previas en checkDni:
		# y checkletra => ha de ser privado
		parteNumericaDni = int( self.dni[:-1] )
		posicion = parteNumericaDni % 23
		return self.tabla.getLetra(posicion)
	



if __name__ == 	'__main__':

	'''
	tabla = TablaAsignacion()
	print(tabla.getLetra(1))
	letras = ['I', 'Ñ', 'O', 'U']
	for letra in letras:
		print(tabla.letraPermitida(letra)) 
	'''

	# meter DNI's en fichero

	cadenas = [ '44453296T', '53179805X', '12345678O', 'A2345678X', '44453296X']

	for dni in cadenas:
		objeto = Dni(dni)
		print(objeto.getDni())
		objeto.checkDni()
		print(objeto.getSano())
		# print(objeto.calcularLetra())
		print('La letra es', objeto.obtenerLetra() )

		# objeto.printTabla()
		# objeto.mostrarTabla() => Como no hay herencia, no funciona


	

