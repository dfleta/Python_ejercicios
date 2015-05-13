# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(lista):

    if lista == []:

        return 0

    else:
    
        numeroMayor = lista[0]

        for elemento in lista:

            if elemento > numeroMayor:

                numeroMayor = elemento

            # else: elemento <= numeroMayor


    return numeroMayor
            
# Casos test
print greatest([4,23,1]) 
# El mayor es 23

print greatest([]) 
# Devuelve 0

print greatest([1,12,45,20]) 
# Devuelve 45


#print greatest([4,23,1])
#>>> 23
    
#print greatest([])
#>>> 0
