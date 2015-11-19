
from class_bcolors_enum import *

def testUnidad(unidad, casosTest):

	''' unidad es el nombre de la funcion
		casosTest es una tupla: (caso test , resultado correcto)'''

	fail = False
	
	for casoTest in casosTest:
		resultado = unidad(casoTest[0])
		if resultado == casoTest[1]:
			print("caso %s => %s" % (casoTest[0], str(resultado)), Colors.OKGREEN + "OK" + Colors.ENDC) 
		else:
			fail = True
			print("caso %s => %s" % (casoTest[0], str(resultado)), Colors.FAIL + "FAIL" + Colors.ENDC) 

	if fail:
		print(Colors.FAIL + "test unidad FAIL" + Colors.ENDC)
	else:
		print(Colors.OKGREEN + "test unidad OK" + Colors.ENDC)

	return