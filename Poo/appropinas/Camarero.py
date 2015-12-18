
from cierreJornada import *
from Empleado import *

class Camarero(Empleado):

	def __init__(self, nombre = "test"):
		Empleado.__init__(self, nombre)	

	def calcularGananciasPropinas(self, cierreJornada):
		return self.getHorasTrabajadasJornada() * cierreJornada.getTotalPropinas() * self.getPorcentajeGanancias() / cierreJornada.getTotalHorasCamareros()

if __name__ == '__main__':
	
	# Configuración de la aplicación

	jornada = CierreJornada()
	jornada.setTotalPropinas(200)
	jornada.setTotalHorasCamareros(15)

	plantillaPersonal = []

	# Creación de los objetos que corresponden a los empleados de nuestro personal

	camarero = Camarero("Barreiro")
	plantillaPersonal.append(camarero)
	camarero.setPorcentajeGanancias(50 /100)
	camarero.setHorasTrabajadasJornada(3)
	#print("Ganacias del camarero %s: %d" % (camarero.getNombre() , camarero.calcularGananciasPropinas(jornada) ) )
	
	for empleado in plantillaPersonal:
		print("Ganancias de %s son %d" %(empleado.getNombre(), empleado.calcularGananciasPropinas(jornada)) )