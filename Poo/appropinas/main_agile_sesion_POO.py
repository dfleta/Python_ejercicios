
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


class Cocinero(Empleado):

	def __init__(self, nombre = "test"):
		Empleado.__init__(self, nombre)		

	def calcularGananciasPropinas(self, cierreJornada):
		return cierreJornada.getTotalPropinas() * self.getPorcentajeGanancias()


class Camarero(Empleado):

	def __init__(self, nombre = "test"):
		Empleado.__init__(self, nombre)	

	def calcularGananciasPropinas(self, cierreJornada):
		return self.getHorasTrabajadasJornada() * cierreJornada.getTotalPropinas() * self.getPorcentajeGanancias() / cierreJornada.getTotalHorasCamareros()


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

	cocinero = Cocinero("Chez")
	plantillaPersonal.append(cocinero)
	cocinero.setPorcentajeGanancias(50 /100)
	#print("Ganacias del cocinero %s: %d" % (cocinero.getNombre(), cocinero.calcularGananciasPropinas(jornada ) ) )

	camarero = Camarero("Barreiro")
	plantillaPersonal.append(camarero)
	camarero.setPorcentajeGanancias(50 /100)
	camarero.setHorasTrabajadasJornada(3)
	#print("Ganacias del camarero %s: %d" % (camarero.getNombre() , camarero.calcularGananciasPropinas(jornada) ) )
	
	camareroPracticas = Becario("El becas")
	plantillaPersonal.append(camareroPracticas)
	camareroPracticas.setHorasTrabajadasJornada(5)
	camareroPracticas.setPropinas(25)
	#print("Ganancias becario %s: %d" % (camareroPracticas.getNombre(), camareroPracticas.calcularGananciaPropinas(jornada) ) )

	for empleado in plantillaPersonal:
		print("Ganancias de %s son %d" %(empleado.getNombre(), empleado.calcularGananciasPropinas(jornada)) )
	# Como podéis observar, en empleado.calcularGananciasPropinas(jornada)
	# trabaja también con objetos de la clase Becario.
	# Hemos cumplido con el Principio de Substitución de Liskov: 
	# “objetos de un programa deberían ser reemplazables por instancias de sus subtipos sin alterar el correcto funcionamiento del programa”.