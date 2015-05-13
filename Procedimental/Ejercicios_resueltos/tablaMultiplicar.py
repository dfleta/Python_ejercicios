
def tablaMultiplicar(numero):
	
	multiplicador = 1
	while multiplicador <= 10:
		print str(multiplicador) +' * ' + str(numero) + ' = ' + str(multiplicador * numero)
		multiplicador = multiplicador + 1

tablaMultiplicar(3)