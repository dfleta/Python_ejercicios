
def checkFilas(sudoku):

    # Precondicion
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"


    for fila in sudoku:

        for (posicion, numero) in enumerate(fila):
        	# enumerate devuelve (offset, item): offset es la posicion del item en la lista (fila) 
        	# y se incrementa automaticamente en 1 en cada iteracion
            # Averiguo si el numero se encuentra en el resto de la fila /lista (siguiente posicion hasta la ultima)
            if numero in fila[posicion + 1:]:
                return False

    return True


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
      print(attr, " => ", checkFilas(casosTestSudoku.__dict__[attr]))
      # mismo codigo que getattr(module, attr)
      # es necesario añadir el espacio de nombres del modulo: casosTestSudoku.irregular 
