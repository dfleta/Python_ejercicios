
from cierreJornada import *
from Empleado import *

class Cocinero(Empleado):

	def __init__(self, nombre = "test"):
		Empleado.__init__(self, nombre)		

	def calcularGananciasPropinas(self, cierreJornada):
		return cierreJornada.getTotalPropinas() * self.getPorcentajeGanancias()

if __name__ == '__main__':
	
	# Configuración de la aplicación

	jornada = CierreJornada()
	jornada.setTotalPropinas(200)
	jornada.setTotalHorasCamareros(15)

	plantillaPersonal = []

	# Creación de los objetos que corresponden a los empleados de nuestro personal

	cocinero = Cocinero("Chez")
	plantillaPersonal.append(cocinero)
	cocinero.setPorcentajeGanancias(50 /100)
	#print("Ganacias del cocinero %s: %d" % (cocinero.getNombre(), cocinero.calcularGananciasPropinas(jornada ) ) )

	for empleado in plantillaPersonal:
		print("Ganancias de %s son %d" %(empleado.getNombre(), empleado.calcularGananciasPropinas(jornada)) )
