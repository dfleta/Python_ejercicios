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

    #if not esMatrizCuadrada(matriz):
    #    return False

    i = 0
    j = 0

    while i <= len(matriz) - 1:

        while j <= len(matriz[i]) - 1:

            if matriz[i][j] != - matriz[j][i]:

                return False

            j += 1

        i += 1

    return True


# Test Cases:

print(esAntisimetrica([[0, 1, 2],
                       [-1, 0, 3],
                       [-2, -3, 0]]))
# >>> True

print(esAntisimetrica([[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]))
# >>> True

print(esAntisimetrica([[0, 1, 2],
                       [-1, 0, -2],
                       [2, 2, 3]]))
# >>> False

print(esAntisimetrica([[1, 2, 5],
                       [0, 1, -9],
                       [0, 0, 1]]))
# >>> False


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada:

matriz5 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print(esAntisimetrica(matriz5))
# >>>False

matriz6 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print(esAntisimetrica(matriz6))
# >>>False

matriz7 = [[1, 0, 0, 0],
           [0, 1, 0],
           [0, 0, 0, 1]]

print(esAntisimetrica(matriz7))
# >>>False


# casos test matriz cuadrada:

print("casos test matriz cuadrada:")

matriz5 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print(esMatrizCuadrada(matriz5))
# >>>False

matriz6 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print(esMatrizCuadrada(matriz6))
# >>>False

matriz7 = [[1, 2, 3, 4],
           [-2, 1, 5],
           [-3, -5, 1, 1]]

print(esMatrizCuadrada(matriz7))
# >>>False

matriz8 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

print(esMatrizCuadrada(matriz8))
# >>> True
