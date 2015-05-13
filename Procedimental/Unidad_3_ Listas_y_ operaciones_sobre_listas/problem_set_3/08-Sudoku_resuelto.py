# encoding: utf-8

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
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

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,2]]

incorrect2 = [[1,2,3,4],
              [2,3,1,2],
              [4,1,2,3],
              [2,3,1,4]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

irregular = [[1,2,3],
             [2,3,1]]            

def esCuadrado(sudoku):

  numeroFilas = len(sudoku)

  for fila in sudoku:

    if len(fila) != numeroFilas:
        return False      

  return True



def checkNumerosValidos(sudoku):

    # precondiciones

    for fila in sudoku:
      for numero in fila:

          try:
            assert isinstance(numero, int)

          except AssertionError:
                  return False


    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:

      for numero in fila:

          if numero not in numerosValidos:
            return False

    return True



def checkFilas(sudoku):

    for fila in sudoku:

        posicionNumero = 0

        for numero in fila:
            # Averiguo si el numero se encuentra en el resto de la fila /lista (siguiente posicion hasta la ultima)
            if numero in fila[posicionNumero+1:]:
                return False
            else:
                posicionNumero += 1

    return True




def checkColumnas(sudoku):

    primeraFila = sudoku[0]
 
    numeroDeFilas = len(primeraFila) - 1

    for numero in primeraFila:

        indexFilaActual = 0

        # Buscamos cada elemento de la primera fila en el resto de filas:
        # Si el indice que ocupa en las otras filas es igual al que ocupa en la primera: mal <=>
        # <=> no puede haber dos numeros iguales en la misma columna.
        while indexFilaActual < numeroDeFilas:

            indexFilaSiguiente = indexFilaActual + 1

            try:
                # El elemento puede no existir en la fila siguiente: 
                # index devuelve excepcion: ValueError = mensaje "x is not in list"
                # Imposible alcanzar esta excepcion si checkColumnas se ejecuta despues de checkFilas
                posicionNumeroFilaSiguiente = sudoku[indexFilaSiguiente].index(numero)

            except ValueError:
                      # Este bloque de codigo se ejecuta si sudoku[indexFilaSiguiente].index(numero)
                      # devuelve un error <=> si el numero no esta en la fila
                      return False

            else:
                # Este bloque de codigo se ejecuta si la sentencia sudoku[indexFilaSiguiente].index(numero)
                # ha ido bien <=> el numero esta en la fila
                if posicionNumeroFilaSiguiente == primeraFila.index(numero):
                      return False
                else:
                      indexFilaActual += 1

    return True
 


def check_sudoku(sudoku):
    
    return esCuadrado(sudoku) and checkNumerosValidos(sudoku) and checkFilas(sudoku) and checkColumnas(sudoku)


# Casos test:

# print checkFilas(correct)
#>>> True
# print checkFilas(incorrect)
#>>> False

# print checkColumnas(correct)
#>>> True
# print checkColumnas(incorrect2)
#>>> False

print check_sudoku(irregular)
#>>> False
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False


