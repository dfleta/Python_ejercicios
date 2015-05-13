# encoding: UTF-8
# Autor: Daniel de Miguel Orell

def mayorMenorMedia(numeroDeElementos):
    

    mayor = input('Introduce el primer número de la serie:')
    menor = mayor #inicializamos las variables
    suma = mayor

    numerosPorProcesar = numeroDeElementos - 1 #creamos un numerosPorProcesar
    
    while numerosPorProcesar > 0:

        nuevoNumero = input('Introduce el siguiente número de la serie:')
        
        if mayor < nuevoNumero:
            mayor = nuevoNumero
        elif menor > nuevoNumero:
            menor = nuevoNumero
        # else: descartamos el número de la serie
            
        suma = suma + nuevoNumero # usaremos suma para calcular la media

        numerosPorProcesar = numerosPorProcesar - 1

    media = suma / float(numeroDeElementos)

    return mayor, menor, media

mayor, menor, media = mayorMenorMedia(input('Introduce el número de elementos que tendra la serie:'))

print mayor
print menor
print media

#Test1 1, 2, 3, 4 = (4, 1, 2.5)
#Test2 6, 5, 9, 2 = (9, 2, 5.5)
#Test3 -2, 9, 5.5 = (9, -2, 4.16666666666666)