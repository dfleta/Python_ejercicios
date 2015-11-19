# Equacion segundo grado : ax^2 + bx + c = 0
# a es el coeficiente cuadratico (distinto de 0)
# b el coeficiente lineal 
# c es el termino independiente

def equacionSegundoGrado(a, b, c):

	import math


	discriminante = b**2 - 4*a*c
	
	if  a != 0  and  discriminante >= 0:
	
		resultadoRaizCuadrada = math.sqrt(discriminante)
	
		x1 = (-b + resultadoRaizCuadrada) / (2 * a)
		x2 = (-b - resultadoRaizCuadrada) / (2 * a)
			
		return x1, x2

	else:
		return None


# casos test
a = -1
b = -2
c = -1

# si a = 0 => no existe solucion real
a =  0
b = -2
c = -1
if None == equacionSegundoGrado(a, b, c):
	print("PASS a = 0")
else:
	print("FAIL a = 0")

# si b = 0 y -c/a < 0 => no existe solucion real
a = -1
b =  0
c = -1
if None == equacionSegundoGrado(a, b, c):
	print("PASS a = 0 AND -c/a < 0")
else:
	print("FAIL a = 0 AND -c/a < 0")

# si b = 0 y c = 0 => x1 = x2 = 0
a = -1
b =  0
c =  0
x1, x2 = equacionSegundoGrado(a, b, c)
if x1 == 0 and x2 == 0:
    print("PASS b = 0 y c = 0")
else:
	print("FAIL b = 0 y c = 0")

# si c = 0 => x1 = 0 and x2 = -b/a
a = -1
b = -2
c =  0
desviacion = 0.01
x1, x2 = equacionSegundoGrado(a, b, c)

if b > 0:
	raizNula   = x1
	raizNoNula = x2
else:
	raizNula   = x2
	raizNoNula = x1

if raizNula == 0 and -b/a + desviacion >= raizNoNula >= -b/a - desviacion :  # ejemplo depuracion
	print("PASS c = 0")
else:
	print("FAIL c = 0") 

# los siguientes casos test no son optimos: pocos y no automatizados

casosTest = [((-1, -2, -1), (-1.0, -1.0)),
             ((-1, -5, -2), (-4.56155281281, -0.438447187191)),
             ((4, 8, 2), (-0.29, -1.71)),
             ((7.7, 9.9, 2.2), (-0.29, -1.0))]

desviacion = 0.01
for casoTest in casosTest:
	x1, x2 = equacionSegundoGrado(*casoTest[0])
	if  casoTest[1][0] + desviacion >= x1 >= casoTest[1][0] - desviacion and casoTest[1][1] + desviacion >= x2 >= casoTest[1][1] - desviacion:
		print("PASS caso test: ", casoTest)
	else:
		print("FAIL caso test: ", casoTest)
