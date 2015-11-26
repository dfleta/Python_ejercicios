# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is esAntisimetrica and False otherwise. 
# An nxn square is called esAntisimetrica if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def esAntisimetrica(matriz):
    
    assert len(matriz) == len(matriz[0])

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

print esAntisimetrica([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print esAntisimetrica([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print esAntisimetrica([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print esAntisimetrica([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

# casos test que no satisfacen la precondicion de que la matriz sea cuadrada:

matriz4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print esAntisimetrica(matriz4)
#>>>False

matriz5 = [[1,0,0,0,0,0,0,0,0]]

print esAntisimetrica(matriz5)
#>>>False 