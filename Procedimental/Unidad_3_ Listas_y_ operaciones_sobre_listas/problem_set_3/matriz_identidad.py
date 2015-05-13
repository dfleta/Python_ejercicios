# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0. 
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)

def esMatrizIdentidad(matrix):
    # Escribe tu codigo aqui



# Casos test:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print esMatrizIdentidad(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print esMatrizIdentidad(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print esMatrizIdentidad(matrix3)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

print esMatrizIdentidad(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print esMatrizIdentidad(matrix7)
#>>>False           


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print esMatrizIdentidad(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print esMatrizIdentidad(matrix5)
#>>>False           