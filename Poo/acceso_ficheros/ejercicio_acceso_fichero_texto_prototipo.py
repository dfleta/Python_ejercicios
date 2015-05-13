
'''
myfile = open('datos_prototipo.txt')				# Open for text input: 'r' is default
linea = myfile.readline()

linea = linea.rstrip()  # quita \n
linea = linea.split()

print(linea)
lineas = myfile.readlines()
'''

def toInt(lista):
	listaConvertida = []
	for item in lista:
		if item.isdigit():
			listaConvertida.append( int(item) )
		else:
			listaConvertida.append( item )
	return listaConvertida

listaRegistros = [ linea.rstrip().split() for linea in open('datos_prototipo.txt') ] 	# devolver una lista de tuplas 

# coleccionPargs = [ int(item) for registro in listaRegistros[1:] for item in registro if item.isdigit()  ]
# print( coleccionPargs )


listaRegistrosConvertida = list( map(toInt, listaRegistros ) )

print( listaRegistrosConvertida )

listaTuplas = [ tuple(item) for item in listaRegistrosConvertida[1:] ]

print( listaTuplas )


# version 2

def toInt(lista):
	return [ int( item ) if item.isdigit() else item for item in lista ]

listaRegistros = [ linea.rstrip().split() for linea in open('datos_prototipo.txt') ]

listaRegistrosConvertida = list ( map(toInt, listaRegistros ) )

listaTuplas = [ tuple(item) for item in listaRegistrosConvertida[1:] ]

print( listaTuplas )


# version 3

listaRegistros = [ linea.rstrip().split() for linea in open('datos_prototipo.txt') ]

listaRegistrosConvertida = [  tuple( int(item) if item.isdigit() else item for item in lista )  for lista in listaRegistros  ][1:]

print( listaRegistrosConvertida )

# version 4

listaRegistrosConvertida = [  tuple( int(item) if item.isdigit() else item for item in lista )  for lista in [ linea.rstrip().split() for linea in open('datos_prototipo.txt') ]  ][1:]

print( listaRegistrosConvertida )

# version 5

matriz = [ linea.rstrip().split() for linea in open('datos_prototipo.txt') ]

matriz = [ tuple( int(item) if item.isdigit() else item for item in row ) for row in matriz ][1:]

print(matriz)

