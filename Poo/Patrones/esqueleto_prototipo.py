
class Persona:
	def __init__(self, nombre = "proto", horas = 0, rate = 0):
		self.__nombre = nombre


class Plantilla:

	def __init__(self, datos, Componente):
		self.__plantilla = []

	def crearPlantilla(self):
		...
		prototipoPersona = Componente() 
		# creamos el prototipo

		for item in datos:
			self.__listaPlantilla.append( prototipoPersona.__class__( item, 'horas', 'rate' ) )



def main():
	data = {'John': 
				{'horas': 2,
				 'rate': 25},
		'Paul': 
				{'horas': 2,
				 'rate': 25},
		'Ringo': 
				{'horas': 2,
				 'rate': 5},
		'George': 
				{'horas': 2,
				 'rate': 15},
		}

	personal = Plantilla(data, Persona)

	personal.crearPlantilla()

	personal.mostrarPlantilla()

	print(personal)

main()