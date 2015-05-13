# encoding = utf-8


def euros(cantidad):
    
    assert cantidad >= 0
    assert isinstance(cantidad, int)

    numeroDeMonedas = [0, 0, 0]

    tiposDeMonedas = [5, 2, 1]

    
    resto = cantidad

    posicionTiposDeMonedas = 0

    while resto != 0:

        numeroDeMonedas[posicionTiposDeMonedas] = resto / tiposDeMonedas[posicionTiposDeMonedas] # // Division entera en python3.0
        
        resto = resto % tiposDeMonedas[posicionTiposDeMonedas]

        posicionTiposDeMonedas = posicionTiposDeMonedas + 1
    

    return numeroDeMonedas




print euros(8)
#>>> (1, 1, 1)  # una de 5 cents, una de 2 cents y una de 1 cent.
print euros(5)
#>>> (1, 0, 0)  # una 5 cents, ninguna de 2 cents y ninguna de 1 cent.
print euros(29)
#>>> (5, 2, 0)  # cinco de 5 cents, dos de 2 cents y ninguna de 1 cent.
print euros(0)
#>>> (0, 0, 0) # ninguna de 5 cents, ninguna de 2 cents y 1 de cents.
