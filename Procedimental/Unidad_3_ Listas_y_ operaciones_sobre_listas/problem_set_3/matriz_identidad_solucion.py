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

    if not esMatrizCuadrada(matrix):
        return False

    posicionUnoCorrecta = 0

    contadorUnos = 0
    contadorFalsos = 0

    for fila in matrix:

        for elemento in fila:

            if elemento == 1:

                posicionUno = fila.index(elemento)
                contadorUnos += 1

            elif elemento != 0:

                contadorFalsos += 1

            # else: el numero es un cero y continua el procesamiento

        if contadorUnos != 1 or contadorFalsos != 0 or posicionUno != posicionUnoCorrecta:
            return False

        contadorUnos = 0
        posicionUnoCorrecta += 1

    return True


# Casos Test:

matrix1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]

print(esMatrizIdentidad(matrix1))
# >>>True

matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

print(esMatrizIdentidad(matrix2))
# >>>False

matrix8 = [[1, 0, 1],
           [0, 1, 0],
           [0, 0, 0]]

print(esMatrizIdentidad(matrix8))
# >>>False

matrix3 = [[2, 0, 0],
           [0, 2, 0],
           [0, 0, 2]]

print(esMatrizIdentidad(matrix3))
# >>>False

matrix6 = [[1, 0, 0, 0],
           [0, 1, 0, 2],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]

print(esMatrizIdentidad(matrix6))
# >>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]

print(esMatrizIdentidad(matrix7))
# >>>False


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada:

matrix4 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print(esMatrizIdentidad(matrix4))
# >>>False

matrix5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print(esMatrizIdentidad(matrix5))
# >>>False

matrix9 = [[1, 0, 0, 0],
           [0, 1, 0],
           [0, 0, 0, 1]]

print(esMatrizIdentidad(matrix9))


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

matriz7 = [[1, 0, 0, 0],
           [0, 1, 0],
           [0, 0, 0, 1]]

print(esMatrizCuadrada(matriz7))
# >>>False

matriz8 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

print(esMatrizCuadrada(matriz8))
# >>> True
