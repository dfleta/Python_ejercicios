
# Criba de Erastotenes:
# Lee el algoritmo en:
# http://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes
# http://recursostic.educacion.es/descartes/web/materiales_didacticos/divisibilidad/numeros_primos_y_numeros_compues.htm

# La criba de Eratóstenes es un algoritmo que permite hallar todos los números primos menores 
# que un número natural dado n. Se forma una tabla con todos los números naturales comprendidos
# entre 2 y n, y se van tachando los números que no son primos de la siguiente manera: 
# Comenzando por el 2, se tachan todos sus múltiplos; comenzando de nuevo, cuando se encuentra 
# un número entero que no ha sido tachado, ese número es declarado primo, y se procede a tachar todos sus múltiplos, 
# así sucesivamente. 
# El proceso termina cuando el cuadrado del mayor número confirmado como primo es mayor que n.


def numerosPrimos(hastaNumero):

	# La funcion recibe un numero hasta el que calcular los primos

	# Generamos la lista desde el 2 en adelante, ya que el 1 no es primo

	listaNumeros = list(range(2,hastaNumero))


	# Cogemos la criba con el siguiente numero de la lista, que siempre sera un numero primo

	for primo in listaNumeros:

			# Dividimos el resto de numeros de la lista por el primo

			posicionPrimo = listaNumeros.index(primo)

			for numero in listaNumeros[ posicionPrimo+1 : ]:

				# Si el numero es divisible por el primo entonces lo eliminamos de la lista.

				if numero % primo == 0:
					listaNumeros.remove(numero)

			# Podemos optimizar el algoritmo deteniendo el proceso cuando el cuadrado del ultimo numero
			# considerado primo es mayor que el numero limite que le pasamos a la funcion

			if primo**2 > hastaNumero:
				break

	# Devolvemos una lista con los numeros que han sobrevivido a la criba

	return listaNumeros




# Casos test: puede hacerse

numerosPrimosMenoresCien = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

numerosLimite = [20, 50, 100]

for numeroLimite in numerosLimite:

	listaPrimosMenoresNumero = numerosPrimos(numeroLimite)

	i = 0
	
	while i < len(listaPrimosMenoresNumero): 
	
			if listaPrimosMenoresNumero[i] == numerosPrimosMenoresCien[i]:
				listaCorrecta = True
				i += 1
			else:
				listaCorrecta = False
				print('Malo =', listaPrimosMenoresNumero[i])
				break

	print('OK = ', listaCorrecta)

	print(listaPrimosMenoresNumero)