# Dada una lista de listas representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0.
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)


def esMatrizCuadrada(matrix):

    numeroFilas = len(matrix)

    for fila in matrix:

        if len(fila) != numeroFilas:
            return False

    return True


def esMatrizIdentidad(matrix):

    # Precondicion: gestion de errores
    # Riesgo de perder lógica del programa al eliminar aserciones en codigo de produccion
    # (no siempre han de eliminarse)
    #
    # assert esMatrizCuadrada(matrix)
    #
    # The public methods assume the data is unsafe,
    # and they are responsible for checking the data (and sanitizing it).

    UNO = 1
    CERO = 0

    if not esMatrizCuadrada(matrix):
        return False

    posicionUnoCorrecta = 0

    contadorUnos = 0
    contadorFalsos = 0

    for fila in matrix:

        for elemento in fila:

            if elemento == UNO:

                posicionUno = fila.index(elemento)
                contadorUnos += 1

            elif elemento != CERO:

                contadorFalsos += 1

            # else: el numero es un cero y continua el procesamiento

        if contadorUnos != 1 or contadorFalsos != 0 or posicionUno != posicionUnoCorrecta:
            return False

        contadorUnos = 0
        posicionUnoCorrecta += 1

    return True


if __name__ == '__main__':
    # Casos Test:

    matrix1 = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    assert esMatrizIdentidad(matrix1) is True

    matrix2 = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 0]]

    assert esMatrizIdentidad(matrix2) is False

    matrix8 = [[1, 0, 1],
               [0, 1, 0],
               [0, 0, 0]]

    assert esMatrizIdentidad(matrix8) is False

    matrix3 = [[2, 0, 0],
               [0, 2, 0],
               [0, 0, 2]]

    assert esMatrizIdentidad(matrix3) is False

    matrix6 = [[1, 0, 0, 0],
               [0, 1, 0, 2],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    assert esMatrizIdentidad(matrix6) is False

    matrix7 = [[1, -1, 1],
               [0, 1, 0],
               [0, 0, 1]]

    assert esMatrizIdentidad(matrix7) is False


    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada:

    matrix4 = [[1, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 1]]

    assert esMatrizIdentidad(matrix4) is False

    matrix5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert esMatrizIdentidad(matrix5) is False

    matrix9 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

    assert esMatrizIdentidad(matrix9) is False


    # casos test matriz cuadrada:
    assert esMatrizCuadrada([[1, 0, 0, 0],
                             [0, 1, 1, 0],
                             [0, 0, 0, 1]]) is False

    assert esMatrizCuadrada([[1, 0, 0, 0, 0, 0, 0, 0, 0]]) is False

    assert esMatrizCuadrada([[1, 0, 0, 0],
                             [0, 1, 0],
                             [0, 0, 0, 1]]) is False

    assert esMatrizCuadrada([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]) is True

    print("All tests passed")