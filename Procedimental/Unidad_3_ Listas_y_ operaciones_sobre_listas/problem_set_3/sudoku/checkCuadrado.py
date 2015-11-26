
def checkCuadrado(sudoku):

	# Precondicion
	assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

	sudokuSano = True
	numeroFilas = len(sudoku)

	for fila in sudoku:
		
		if len(fila) != numeroFilas:
			sudokuSano = False
			break

	# Postcondicion
	assert isinstance(sudokuSano, bool), "la interfaz exige devolver un valor lógico"

	return sudokuSano


### CASOS TEST ###

if __name__ == '__main__':
	
	import casosTestSudoku

	for attr in sorted(casosTestSudoku.__dict__):
	# Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
	# Asi podemos añadir todos los casos que queramos en la unidad cassTestSudoku
	# sin modificar este codigo
		if attr.startswith('__'):
			pass
			# Skip atributo
		else:
			print(attr, " => ", checkCuadrado(casosTestSudoku.__dict__[attr]))
			# mismo codigo que getattr(module, attr)
			# es necesario añadir el espacio de nombres del modulo: casosTestSudoku.irregular	
