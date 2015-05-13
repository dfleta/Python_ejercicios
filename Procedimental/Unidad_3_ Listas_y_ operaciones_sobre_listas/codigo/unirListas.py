# encoding: UTF-8

def unirListas(listaP, listaQ):
	
	for elemento in listaQ:

		if elemento not in listaP:
			listaP.append(elemento)
		# else:
			# el elemento ya existe en la listaP y no lo añadimos
	return

listaA = [1, 2, 3]
listaB = [3, 4, 5]

unirListas(listaA, listaB)
print listaA