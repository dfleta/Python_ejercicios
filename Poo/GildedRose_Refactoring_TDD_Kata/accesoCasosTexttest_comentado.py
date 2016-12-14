
# pag. 282 | Chapter 9: Tuples, Files, and Everything Else - Learning Python 5th Ed.
# pag. 400 | Chapter 13: while and for Loops - Learning Python 5th Ed.


def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):
    """
    Devuelve el conjunto de casos test en una matriz donde cada
    entrada es una matriz con todos los items modificados ese dia:
    matrizCasosTest = [casosTestDia1, casosTestDia2, ... ]

    Los casos test del dia forman una matriz donde cada fila es un item:
    casosTestDia = [item, item, ... ]

    item = ['Elixir of the Mongoose', ' 5', ' 7']

    Argumentos:
    matrizCasosTest = [[dia0], [dia1], ... , [diaN]]

    dia = [
            [item],
            [item],
             ... ]
           ]

    dia = [
            ['Elixir of the Mongoose', ' 5', ' 7'],
            ['Elixir of the Mongoose', ' 5', ' 7'],
             ... ]
           ]
    """
    try:
        # si la ruta de acceso al fichero no es
        # un string lanzamos excepcion de argumento invalido
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        # intentamos abrir el fichero
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        # si el fichero no existe capturamos la excepcion
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []
    else:
        # inicializamos la matriz con todos los casos test
        matrizCasosTest = []
        for linea in fichero:
            # Cada linea del fichero es un item
            # o indica cuando comienzan o terminan los items
            # modificados ese dia
            if linea.find("day") != -1:
                # comienza un nuevo conjunto de casos test a incluir en un dia
                casosTestDia = []
            elif linea == "\n":
                # fin de los items de un dia, fin del caso test del dia
                # incluimos ese conjunto de casos test del dia en el
                # conjunto de casos test = matriz de casos test
                matrizCasosTest.append(casosTestDia)
            elif linea.find("sellIn") != -1:
                # La linea con el nombre de las propiedades indica
                # el numero de propiedades del item
                numeroPropiedadesItem = len(linea.split(','))
            else:
                # Eliminamos end-of-line character \n con rstrip()
                # Si la linea contiene sulfuras, hay una primera coma incluida
                # en el nombre del item: dividimos comenzando por la derecha
                # rsplit() y fijamos un máximo de tantas divisiones como
                # propiedades posean los items.
                # To chop up the line on its comma delimiters split(',')
                # The result is a list of substrings containing the individual
                # Ojo que convierte todo a caracteres (ya no son enteros)!!
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem-1)                # El item forma parte del caso test "día"
                casosTestDia.append(item)
        # cerramos el fichero
        fichero.close()
        return matrizCasosTest


def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):
    """
    Vuelca los casos test cargados en memoria
    a un fichero stdout.txt para inspeccionarlos.
    """
    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            print("La ruta de acceso al fichero ha de ser un string")
    else:
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                stdout.write(','.join(item) + '\n')
        stdout.close()


def mostrarCasosTest(matrizCasosTest):
    """
    Muestra en consola los casos test cargados en memoria
    """
    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)


if __name__ == "__main__":

    rutaAccesoFichero = "./stdout.gr"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    # visualizamos los casos test cargados en memoria:

    mostrarCasosTest(matrizCasosTest)

    # volcamos los casos test cargados en memoria
    # en matrizCasosTest a un fichero stdout.txt
    # para inspeccionarlos comodamente.

    ficheroVolcadoCasosTest = "./stdout.txt"

    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)
