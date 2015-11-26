
def checkNumerosEnRango(sudoku):

    # Precondicion
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"


    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:

      for numero in fila:

          if not isinstance(numero, int) or numero not in numerosValidos:
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
      print(attr, " => ", checkNumerosEnRango(casosTestSudoku.__dict__[attr]))
      # mismo codigo que getattr(module, attr)
      # es necesario añadir el espacio de nombres del modulo: casosTestSudoku.irregular 
