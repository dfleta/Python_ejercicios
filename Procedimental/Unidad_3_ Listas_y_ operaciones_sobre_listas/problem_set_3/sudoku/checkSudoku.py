# encoding: utf-8

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, checkSudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.



def checkSudoku(sudoku):

    # Precondicion
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    from checkCuadrado      import checkCuadrado
    from checkNumerosEnRango import checkNumerosEnRango
    from checkFilas         import checkFilas
    from checkColumnas      import checkColumnas
    
    sudokuSano = checkCuadrado(sudoku) and checkNumerosEnRango(sudoku) and checkFilas(sudoku) and checkColumnas(sudoku)

    # Postcondicion
    assert isinstance(sudokuSano, bool)

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
      print(attr, " => ", checkSudoku(casosTestSudoku.__dict__[attr]))
      # mismo codigo que getattr(module, attr)
      # es necesario añadir el espacio de nombres del modulo: casosTestSudoku.irregular 





