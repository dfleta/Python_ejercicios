
from cierreJornada import *
from Camarero import *

class Becario(Camarero):
	# ¡OJO que ya serían 2 niveles de herencia!

	def __init__(self, nombre):
		Camarero.__init__(self, nombre)
		self.propinas = 0

	def setPropinas(self, totalPropinas):
		self.propinas = totalPropinas

	def getPropinas(self):
		return self.propinas

	def calcularGananciasPropinas(self, jornada):
		return self.getPropinas()


if __name__ == '__main__':
	
	# Configuración de la aplicación

	jornada = CierreJornada()
	jornada.setTotalPropinas(200)
	jornada.setTotalHorasCamareros(15)

	plantillaPersonal = []

	# Creación de los objetos que corresponden a los empleados de nuestro personal

	camareroPracticas = Becario("El becas")
	plantillaPersonal.append(camareroPracticas)
	camareroPracticas.setHorasTrabajadasJornada(5)
	camareroPracticas.setPropinas(25)
	#print("Ganancias becario %s: %d" % (camareroPracticas.getNombre(), camareroPracticas.calcularGananciaPropinas(jornada) ) )

	for empleado in plantillaPersonal:
		print("Ganancias de %s son %d" %(empleado.getNombre(), empleado.calcularGananciasPropinas(jornada)) )