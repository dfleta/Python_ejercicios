# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is esAntisimetrica and False otherwise.
# An nxn square is called esAntisimetrica if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.


def esMatrizCuadrada(matriz):

    numeroFilas = len(matriz)

    for fila in matriz:

        if len(fila) != numeroFilas:
            return False

    return True


def esAntisimetrica(matriz):

    # precondicion: manejo de errores.
    # The public methods assume the data is unsafe,
    # and they are responsible for checking the data (and sanitizing it).

    # validate input: must be a square matrix
    if not esMatrizCuadrada(matriz):
        return False

    # iterate rows and columns, ensuring inner index resets per row
    fila = 0
    while fila < len(matriz):

        columna = 0
        while columna < len(matriz[fila]):

            if matriz[fila][columna] != - matriz[columna][fila]:
                return False

            columna += 1

        fila += 1

    return True



if __name__ == '__main__':
    # Test Cases:

    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, 3],
                             [-2, -3, 0]]) is True

    assert esAntisimetrica([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]) is True

    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, -2],
                             [2, 2, 3]]) is False

    assert esAntisimetrica([ [1, 2, 5],
                             [0, 1, -9],
                             [0, 0, 1]]) is False
    
    assert esAntisimetrica([ [1, 2,  5],
                             [-2, 1, -9],
                             [-5, 0, 1]]) is False


    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada:
    matriz5 = [[1, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 1]]

    assert esAntisimetrica(matriz5) is False

    matriz6 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert esAntisimetrica(matriz6) is False

    matriz7 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

    assert esAntisimetrica(matriz7) is False


    # casos test matriz cuadrada:
    assert esMatrizCuadrada([[1, 0, 0, 0],
                            [0, 1, 1, 0],
                            [0, 0, 0, 1]]) is False

    assert esMatrizCuadrada([[1, 0, 0, 0, 0, 0, 0, 0, 0]]) is False

    assert esMatrizCuadrada([[1, 2, 3, 4],
                            [-2, 1, 5],
                            [-3, -5, 1, 1]]) is False

    assert esMatrizCuadrada([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]) is True

    print("All tests passed")