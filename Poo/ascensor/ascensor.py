
class Ascensor():
	
	def __init__(self, identificador, capacidad, pesoMaximo, plantas):
	
		# el peso se calcula de manera automatica: 80kg por persona
		# al igual que el numero de plantas

		self.identificador = identificador
		self.capacidad = capacidad
		self.pesoMaximo = pesoMaximo
		self.activado = True

		self.personas = 0
		self.peso = 0
		self.piso = 0
		self.emergencia = False

		self.pesoPersona = int( pesoMaximo / capacidad )  # +1
		self.plantas = ['S'] + list( range(plantas + 1) ) # +1
	
	def __repr__(self):
		return '%s: %s' % (self.__class__.__name__, self.obtenerAtributos()) # +1
	
	def obtenerAtributos(self):
		atributos = []
		for key in sorted( self.__dict__ ):
			atributos.append( '%s = %s ' % (key, self.__dict__[key]) ) # +1
		return atributos

	def checkRep(self): 												# +1
		assert 0 <= self.personas <= 6
		assert 0 <= self.peso     <= self.pesoMaximo
		assert self.piso in self.plantas

	def mostrarInfoAscensor(self):
		# self.__repr__()												# +1
		for key in sorted ( self.__dict__) :
			print(key, ' = ', self.__dict__[key])

	def ascensorActivado(self):
		return not self.emergencia

	def activarAscensor(self):
		self.activado = True

	def desactivarAscensor(self):
		self.activado = False

	def subePersona(self, numeroPersonas):
		self.personas += numeroPersonas
		self.excesoPersonas()
		self.peso = self.personas * self.pesoPersona
		self.excesoPeso()

	def bajaPersona(self, numeroPersonas):
		self.personas -= numeroPersonas
		self.checkRep()
		self.peso = self.personas * self.pesoPersona


	def canviarPlanta(self, piso):
		# el ascensor ha de estar activado
		if not self.ascensorActivado():
			print( 'Ascensor Bloqueado' )
			return None
		if piso == 'S':
			self.piso = self.plantas[0]
		else:
			self.piso = self.plantas[ piso + 1 ]

	def pulsarBotonEmergencia(self):
		self.emergencia = True

	# def mostrarInfoAscensor(self):
	#	print(self)

	def excesoPeso(self):
		if self.peso > self.pesoMaximo:
			print ('¡Alarm! Exceso de peso')

	def excesoPersonas(self):
		if self.personas > self.capacidad:
			print('¡Alarma! Exceso de personas')
		self.desactivarAscensor()

if __name__ == '__main__':
	
	ascensor = Ascensor('123456-SYT', 5, 400, 6)

	ascensor.canviarPlanta(0)
	ascensor.subePersona(3)
	print(ascensor)
	ascensor.canviarPlanta(4)
	ascensor.bajaPersona(2)
	print(ascensor)
	ascensor.canviarPlanta(5)
	# ascensor.pulsarBotonEmergencia()
	ascensor.bajaPersona(1)
	ascensor.canviarPlanta(0)
	# ascensor.mostrarInfoAscensor()
	print(ascensor)

'''
para testear el examen:

deben proveer:
 getPersonas
 getPeso 
 getPiso
 getEmergencia

yo aplico la serie que esta aqui en el test y uso esos metodos
para saber si el resultado es correcto
hacer dos casos test: uno con secuencia normal, otro con pulsarBotonEmergencia
'''

