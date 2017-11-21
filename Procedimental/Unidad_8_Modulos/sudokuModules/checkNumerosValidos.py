
# -*- coding: iso-8859-15 -*-


def sonNumerosEnteros(sudoku):

    for fila in sudoku:

        for numero in fila:

            if not isinstance(numero, int):
                return False

    return True


def numerosEnRango(sudoku):

    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:

        for numero in fila:

            if numero not in numerosValidos:
                return False

    return True


def checkNumerosValidos(sudoku):

    # precondiciones

    return sonNumerosEnteros(sudoku) and numerosEnRango(sudoku)


### CASOS TEST ###

if __name__ == '__main__':

    import casosTestSudoku

    for attr in sorted(casosTestSudoku.__dict__):
        # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
        # Asi podemos añadir todos los casos que queramos
        # en la unidad cassTestSudoku sin modificar este codigo
        if attr.startswith('__'):
            pass
            # Skip atributo
        else:
            print(attr, " => ", checkNumerosValidos(casosTestSudoku.__dict__[attr]))
            # mismo codigo que getattr(module, attr)
            # es necesario añadir el espacio de nombres del modulo:
            # casosTestSudoku.irregular
