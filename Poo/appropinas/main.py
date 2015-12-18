
from cierreJornada  import *
from Empleado 		import *
from Cocinero 		import *
from Camarero 		import *
from Becario 		import *


def main():

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


if __name__ == '__main__':
	
	main()


	