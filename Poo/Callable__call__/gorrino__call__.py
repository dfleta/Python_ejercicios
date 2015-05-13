

# crear un objeto hucha de la clase gorrino que admita la sintaxis hucha(dinero) 

class Gorrino:
	def __init__(self, value):
		self.value = value
	def __call__(self, other):
		self.value = self.value + other
	def romper(self):
		return self.value
	# def meter(self, other):
	# 	self.value = self.value + other

	# comentario sobre el metodo del()
	# No es necesario: python destruye el objeto cuando cambiamos su referencia:
	# hucha = Gorrino(0) y más tarde hucha = Gorrino(20) => destruccion
	# Para ejecutar acciones al destruir o finalizar => mejor try /except/ FINALLY
	# esto esta explicado en el capitulo sobre sobrecarga de operadores en el libro de Python Lutz
	# def __del__(self):

hucha = Gorrino(0)

for i in range(1,5):
	hucha(10)
	# hucha.meter(10)

print(hucha.romper())
# 40



class Gorrino:
	
	def __init__(self, *pargs):		# collect in a tuple by * => empaqueta los parametros en una tupla
		self.value = self.sumar(pargs) 	# pasa los parametros como una tupla
	
	def __call__(self, *pargs):
		self.value = self.value + self.sumar(pargs)
	
	def romper(self):
		return self.value

	def sumar(self, pargs):
		suma = 0
		for arg in pargs:
			suma = suma + arg
		return suma


hucha = Gorrino(100)

for i in range(1,4):
	hucha( 20, 10, 5, 2, 1, 1, 1 )
	# hucha.meter(10)

print(hucha.romper())
# 40


# otra version con unpack: *

class Gorrino:
	
	def __init__(self, *pargs):		# collect in a tuple by * => empaqueta los parametros en una tupla
		self.value = self.sumar(*pargs) 	# * usado en la invocacion de una funcion desempaqueta la coleccion => (2)
	
	def __call__(self, *pargs):
		self.value = self.value + self.sumar(*pargs) # * usado en la invocacion de una funcion desempaqueta la coleccion

	def romper(self):
		return self.value

	def sumar(self, *pargs):		# (2) por tanto es necesario volver a empaquetar los argumentos en una coleccion para recorrerla
		suma = 0
		for arg in pargs:
			suma = suma + arg
		return suma


hucha = Gorrino(100)

for i in range(1,4):
	hucha( 20, 10, 5, 2, 1, 1, 1 )
	# hucha.meter(10)

print(hucha.romper())
# 40





'''
def paso(*pargs):  # empaqueta los parametros en una tupla
	print(pargs)   # pasa los parametros como una tupla
	return prueba(pargs)
 
def prueba(pargs): # recoge la tupla => sin * para no volver a empaquetarlos en una tupla	
	suma = 0
	print(pargs)
	for arg in pargs:
		print(arg)
		suma = suma + arg
	return suma
print('prueba =', paso(10, 5, 5))
'''
