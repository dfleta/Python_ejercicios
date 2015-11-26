
def checkColumnas(sudoku):

   # Precondicion
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    primeraFila = sudoku[0]
 
    numeroDeFilas = len(sudoku) - 1

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
                      # devuelve un error <=> si el numero no esta en la fila siguiente
                      # no llegaria a presentarse el caso pues checkNumerosEnRango se ejecuta antes
                      return False

            else:
                # Este bloque de codigo se ejecuta si la sentencia sudoku[indexFilaSiguiente].index(numero)
                # ha ido bien <=> el numero esta en la fila
                if posicionNumeroFilaSiguiente == primeraFila.index(numero):
                      return False
                else:
                      indexFilaActual += 1

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
      print(attr, " => ", checkColumnas(casosTestSudoku.__dict__[attr]))
      # mismo codigo que getattr(module, attr)
      # es necesario añadir el espacio de nombres del modulo: casosTestSudoku.irregular 
