# coding = utf-8


# Define un prodecimiento, euros, que toma como entrada un entero positivo en euros
# y devuelve el número de monedas de 5 céntimos, de 2 cénts. y de 1 cénts. requeridos 
# para formar ese valor. El valor retornado debe ser una lista de tres números:
# el número de monedas de 5 cénts, de 2 cénts. y de 1 cénts. necesarias.
#
# Tu respuesta debe usar el menor número posible usandp primero cuantas más monedas
# de 5 cénts posible, luego de 2 y finalmente de 1 (para sumar el total)
#


def euros(cantidad):

    tiposDeMonedas = [5, 2, 1]

    numeroDeMonedas = [0, 0, 0]

    i = 0
    
    for moneda in tiposDeMonedas:

            numeroDeMonedas[i] = cantidad // moneda # en python 3 necesitamos // para divisiones enteras
            cantidad = cantidad % moneda

            if cantidad  == 0:
                break
            else:
                i += 1

    return numeroDeMonedas



print(euros(8))
#>>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
print(euros(5))
#>>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(euros(29))
#>>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
print(euros(0))
#>>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.
