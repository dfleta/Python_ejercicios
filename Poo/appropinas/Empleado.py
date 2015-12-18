
from cierreJornada import *

class Empleado:

	def __init__(self, nombre = "test"):
		self.nombre = nombre
		self.porcentajeGanancias = 0
		self.horasTrabajadasJornada = 0

	def setNombre(self, nombre):
		self.nombre = nombre

	def getNombre(self):
		return self.nombre

	def setHorasTrabajadasJornada(self, horasTrabajadasJornada):
		self.horasTrabajadasJornada = horasTrabajadasJornada 

	def getHorasTrabajadasJornada(self):
		return self.horasTrabajadasJornada

	def setPorcentajeGanancias(self, porcentajeGanancias):
		self.porcentajeGanancias = porcentajeGanancias

	def getPorcentajeGanancias(self):
		return self.porcentajeGanancias

if __name__ == '__main__':
	
	# Configuración de la aplicación

	jornada = CierreJornada()
	jornada.setTotalPropinas(200)
	jornada.setTotalHorasCamareros(15)

	plantillaPersonal = []

	# Los casos test de esta clase requieren conocimientos de diccionarios... y no habéis querido leerlos...
	# En breve los escribo.