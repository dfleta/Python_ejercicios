

class TablaAsignacion:

	# podemos utilizar este ejercicio para sobrecarga de operaciones sobre listas
	def __init__(self):
		self.tabla = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 
						'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]

	def getLetra(self, posicion):
		try:
			return self.tabla[posicion]
		except:
			return 'Posicion letra fuera de rango'

	def getModulo(self):
		return len(self.tabla)

	def letraPermitida(self, letra):
		return letra in self.tabla

	def mostrarTabla(self):
		print(self.tabla)


if __name__ == 	'__main__':

	tabla = TablaAsignacion()
	print(tabla.getLetra(1))
	print(tabla.getLetra(23))
	letras = ['I', 'Ñ', 'O', 'U']
	for letra in letras:
		print('Letra %c:' % letra, tabla.letraPermitida(letra)) 


	

