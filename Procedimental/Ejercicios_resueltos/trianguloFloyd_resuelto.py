# coding=utf-8

def trianguloFloyd(numeroNaturalLimite):

	numeroActual = 1

	fila = 1
	
	while numeroActual <= numeroNaturalLimite:
		
		linea = ""
		columna = 1
		
		while columna <= fila:
			
			linea = linea + '\t' + str(numeroActual)
			
			numeroActual += 1
			columna += 1
		
		print(linea)
		
		fila += 1


# numero = input('Introduce el número natural hasta donde dibujar el triángulo: ')
# trianguloFloyd(numero)

# Casos test: deben estar automatizados.
# Usamos los números triangulares para generar los casos test: aquellos situados en la hipotenusa del triángulo.
# Responden a la serie: n*(n+1)/2 (n es un número natural)

n = 1

while n <= 5:
	trianguloFloyd(n*(n+1)/2)
	print('\t' + '-'*8*(n-1) + '-')
	n += 1
