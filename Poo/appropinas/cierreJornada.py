class CierreJornada:

	def __init__(self):
		self.totalHorasCamareros = 0
		self.totalPropinas 		 = 0

	def setTotalHorasCamareros(self, totalHorasCamareros):
		self.totalHorasCamareros = totalHorasCamareros

	def getTotalHorasCamareros(self):
		return self.totalHorasCamareros

	def setTotalPropinas(self, totalPropinas):
		self.totalPropinas = totalPropinas

	def getTotalPropinas(self):
		return self.totalPropinas

if __name__ == '__main__':
	
	jornada = CierreJornada()
	jornada.setTotalPropinas(200)
	jornada.setTotalHorasCamareros(15)

	print(jornada.getTotalPropinas(), jornada.getTotalHorasCamareros())