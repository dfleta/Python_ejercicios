
from class_bcolors_enum import *

def testUnidad(unidad, casosTest):

	''' unidad es el nombre de la funcion
		casosTest es una tupla: (caso test , resultado correcto)'''

	fail = False
	
	for casoTest in casosTest:
		resultado = unidad(casoTest[0])
		if resultado == casoTest[1]:
			print("caso %s => %d" % (casoTest[0], resultado), bcolors.OKGREEN + "OK" + bcolors.ENDC) 
		else:
			fail = True
			print("caso %s => %d" % (casoTest[0], resultado), bcolors.FAIL + "FAIL" + bcolors.ENDC) 

	if fail == True:
		print(bcolors.FAIL + "test unidad FAIL" + bcolors.ENDC)
	else:
		print(bcolors.OKGREEN + "test unidad OK" + bcolors.ENDC)

	return