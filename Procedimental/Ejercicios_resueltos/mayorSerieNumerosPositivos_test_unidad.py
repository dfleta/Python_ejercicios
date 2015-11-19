"""
19. Lee por teclado 5 números enteros positivos, y escribe cuál es el mayor de los números introducidos.  
20. Repite el programa anterior, pero chequeando que el usuario no introduzca
numeros negativos. Si se da esta circunstancia hay que visualizar un mensaje
de error, forzando al usuario a que introduzca numeros positivos.
"""

from testUnidad import * 


###### RUTINAS ######


def cargarSerieNumerosPositivos(serieNumeros, longitudSerie):
	
	''' Es necesario programar las precondiciones'''

	contador = 0
	while contador < longitudSerie:
	    numero = int( input('Introduce un numero: ') )
	    if numero >= 0:
	    	serieNumeros.append(numero)
	    	contador += 1
	    else:
	    	print("Se descarta el numero negativo")
	return


def calcularMayorSerie(serieNumeros):
	# a modo de precondicion:
	if not serieNumeros:
		return None
	
	numeroMayor = 0
	for numero in serieNumeros:
		if numero > numeroMayor:
			numeroMayor = numero
		else:
			pass
	return numeroMayor


###### MAIN ######

print("Explicacion...")

serieNumeros = []

longitudSerie =  int( input('Introduce la longitud de la serie de numeros positivos: ') )

cargarSerieNumerosPositivos(serieNumeros, longitudSerie)

numeroMayor = calcularMayorSerie(serieNumeros)

if numeroMayor or numeroMayor == 0:
	print("El mayor numero es: ", numeroMayor)
else:
	print("No existe serie de numeros")


###### CASOS TEST ######

# Casos test calcularMayorSerie(serieNumeros):

print("###### Casos Test calcularMayorSerie ######")

casosTest = [([], None),
			 ([0], 0),
			 ([1, 2, 3, 4], 4),
			 ([-1, -2, 3], 3),
			 ([1, 2, 3, 4, 5], 5),
			 ([5, 2, 5, 4, 0], 5),
			 ([5, 5, 5], 5)]


testUnidad(calcularMayorSerie, casosTest)