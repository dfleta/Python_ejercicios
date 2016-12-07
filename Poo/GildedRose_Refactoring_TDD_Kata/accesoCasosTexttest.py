
# pag. 282 | Chapter 9: Tuples, Files, and Everything Else - Learning Python 5th Ed.
# pag. 400 | Chapter 13: while and for Loops - Learning Python 5th Ed.


def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):

    '''
        El conjunto de casos test es una matriz donde cada
        entrada es una matriz con todos los items modificados ese dia:
        matrizCasosTest = [casosTestDia1, casosTestDia2, ... ]

        Los casos test del dia forman una matriz donde cada fila es un item:
        casosTestDia = [item, item, ... ]

        item = ['Elixir of the Mongoose', ' 5', ' 7']

        matrizCasosTest = [
                            [item],
                            [item],
                             ... ]
                           ]
                          ]

        matrizCasosTest = [[
                            ['Elixir of the Mongoose', ' 5', ' 7'],
                            ['Elixir of the Mongoose', ' 5', ' 7'],
                             ... ]
                           ]
                          ]
    '''

    fichero = open(rutaAccesoFichero, 'r')

    # inicializamos la matriz con todos los casos test
    matrizCasosTest = []

    for linea in fichero:
        # cada linea del fichero es un item
        # o indica cuando comienzan o terminan los items
        # modificados ese dia
        if linea.find("day") != -1:
            # comienza un nuevo conjunto de casos test a incluir en un diá
            casosTestDia = []
        elif linea == "\n":
            # fin de los items de un dia, fin del caso test del dia
            # incluimos ese conjunto de casos test del dia en el
            # conjunto de casos test = matriz de casos test
            matrizCasosTest.append(casosTestDia)
        elif linea.find("sellIn") != -1:
            # la linea con el nombre de las propiedades no nos interesa
            pass
        else:
            # eliminamos end-of-line character \n
            item = linea.rstrip()
            # si la linea contiene sulfuras, hay una primera coma incluida
            # en el nombre del item: dividismos comenzando por la derecha
            # rsplit() y fijamos un máximo de 3 divisiones
            if linea.find("Sulfuras") != -1:
                item = item.rsplit(',', maxsplit=2)
            else:
                # to chop up the line on its comma delimiters;
                # the result is a list of substrings containing the individual
                # ojo que convierte todo a caracteres
                item = item.split(',')
            # el item forma parte del caso test "día"
            casosTestDia.append(item)

    return matrizCasosTest


if __name__ == "__main__":

    rutaAccesoFichero = "stdout.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    # visualizamos los casos test cargados en memoria:

    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)

    # volcamos los casos test cargados en memoria
    # en matrizCasosTest a un fichero stdout.txt
    # para inspeccionarlos comodamente:

    stdout = open("stdout.txt", 'w')
    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
        for item in casosTestDia:
            stdout.write(','.join(item) + '\n')
