

class CuentaCorriente:
	
	def __init__(self, nombre, apellidos, direccion, telefono, saldo):
		
		self.nombre 	 	= nombre
		self.apellidos 		= apellidos
		self.direccion 		= direccion
		self.telefono  		= telefono
		self.saldo 			= saldo
		self.numerosRojos 	= False
	
	def __repr__(self):
		return '[%s: %s]' % (self.__class__.__name__, self.__recolectarAtributos())

	def setNombre(self, nombre):
		self.nombre = nombre
	
	def getNombre(self):
		return self.nombre	
	
	def setApellidos(self, apellidos):
		self.apellidos = apellidos
	
	
	def getApellidos(self):
		return self.apellidos
	
	def setDireccion(self, direccion):
		self.direccion = direccion
		
	def getDireccion(self):
		return self.direccion
	
	def setTelefono(self, telefono):
		self.telefono = telefono
	
	
	def getTelefono(self):
		return self.telefono
	
	def getSaldo(self):
		return self.saldo
	
	def retirarDinero(self, importe ):
		self.saldo -= importe
		self.setNumerosRojos()
	
	def ingresarDinero(self, importe):
		self.saldo += importe
		self.setNumerosRojos()
	
	def saldoNegativo(self):
		return self.numerosRojos
	
	def setNumerosRojos(self):
		if self.saldo < 0:
			self.numerosRojos = true
		else:
			self.numerosRojos = false
	
	def consultarCuenta(self):
		# self.__dict__ es un diccionario con las propiedades del objeto
		for atributo in sorted(self.__dict__):
			print("%s : %s" % (atributo, self.__dict__[atributo]) )


	def __recolectarAtributos(self):
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append('%s = %s' % (key, getattr(self, key)))  	# lista de atributo = valor	
		return ', '.join(attrs)


if __name__ == '__main__':

	cuenta = CuentaCorriente("Facundo", "Campazzo", "Bolson Cerrado", "999888777", 300)
	print(cuenta)
	cuenta.consultarCuenta()
