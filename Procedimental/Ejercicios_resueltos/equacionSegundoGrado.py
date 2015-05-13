# Autora: Constanza Miro Ferrer
# constanxa4@gmail.com
# Licencia: GNU-GPL

# Equacion segundo grado : ax^2 + bx + c = 0
# x representa la variable 
# a, b y c son constantes
# a es el coeficiente cuadratico (distinto de 0)
# b el coeficiente lineal 
# c es el termino independiente

def equacionSegundoGrado(a, b, c):

	import math


	argumentoRaizCuadrada = b**2 - 4*a*c
	
	if  a != 0  and  argumentoRaizCuadrada >= 0:
	
		resultadoRaizCuadrada = math.sqrt(argumentoRaizCuadrada)
	
		x1 = (-b + resultadoRaizCuadrada) / (2 * a)
		x2 = (-b - resultadoRaizCuadrada) / (2 * a)
			
		return x1, x2

	else:
		return None


# CASOS TEST

print(equacionSegundoGrado(1, 2, 1))
# 'x1 = -1.0, x2 = 1.0'
print(equacionSegundoGrado(4, 3, 1))
# 'No hay solucion'
print(equacionSegundoGrado(0, 2, 1))
# 'El coeficiente cuadratico debe ser distinto de 0'
print(equacionSegundoGrado(-1, -5, -2))
# 'x1 = -4.56155281281, x2 = 0.438447187191'
print(equacionSegundoGrado(-1, -2, -1))
# 'x1 = -1.0, x2 = 1.0'