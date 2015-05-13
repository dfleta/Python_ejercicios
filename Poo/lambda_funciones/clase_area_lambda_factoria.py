import math

class FiguraGeometrica:

	def __init__(self, parametro_1, parametro_2):
		self.parametro_1 = parametro_1
		self.parametro_2 = parametro_2

	def superficie(self): # ahora utilizar esto para crear una clase abstracta que luego llevara a factoria o DIP
		area = {
				"Cuadrado": 	lambda : self.parametro_1 ** 2,
				"Rectangulo": 	lambda : self.parametro_1 * self.parametro_2,
				"Elipse":		lambda : math.pi * self.parametro_1 * self.parametro_2
		}
		return area[self.__class__.__name__]()


class Rectangulo(FiguraGeometrica):
	pass
	'''
	def __init__(self, parametro_1, parametro_2):
		FiguraGeometrica.__init__(self, parametro_1, parametro_2)
	'''
class Cuadrado(FiguraGeometrica):
	pass

class Elipse(FiguraGeometrica):
	pass

# factoria simple
def factoria(Clase, *pargs, **kargs):
	return Clase(*pargs, **kargs)

for Clase in Cuadrado, Rectangulo, Elipse:
	figura = factoria(Clase, 2, 3)
	print ('El area del ' + figura.__class__.__name__ + ' es: ' + str( figura.superficie() ) )

