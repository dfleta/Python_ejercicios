

def formatearPropiedadesItemInt(item):

    itemFormateado = []

    for propiedad in item:
        try:
            itemFormateado.append(int(propiedad.lstrip()))
            assert isinstance(itemFormateado[-1], int)
        except AssertionError:
            print("la propiedad %s ha de ser integer" % propiedad)
        except ValueError:
            itemFormateado.append(propiedad)

    return itemFormateado


def formatearPropiedadesItemStr(item):
    itemFormateado = []
    for propiedad in item:
        if isinstance(propiedad, int):
            itemFormateado.append(" " + str(propiedad))
        else:
            itemFormateado.append(str(propiedad))
    return itemFormateado


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
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []
    else:
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if linea.find("day") != -1:
                casosTestDia = []
            elif linea == "\n":
                matrizCasosTest.append(casosTestDia)
            elif linea.find("name") != -1:
                numeroPropiedadesItem = len(linea.split(','))
            else:
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem-1)
                itemFormateado = formatearPropiedadesItemInt(item)
                casosTestDia.append(itemFormateado)
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
                itemFormateado = formatearPropiedadesItemStr(item)
                stdout.write(','.join(itemFormateado) + '\n')
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

    mostrarCasosTest(matrizCasosTest)

    ficheroVolcadoCasosTest = "./stdout_saneado.txt"

    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)
