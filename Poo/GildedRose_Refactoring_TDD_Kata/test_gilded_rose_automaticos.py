
from gilded_rose import *
from accesoCasosTexttest import *


def extraerItemsIventario(matrizCasosTest):
    """
    Extrae los items y el estado en el que están el primer dia
    de los casos test y devuelve una lista de items:
    items = [ [item], [item], [item] ]

    Argumentos:
    matrizCasostest -> lista con los casos test. Cada elemento es un dia
    """
    return matrizCasosTest[0]


def crearObjetoItem(item):
    """
    Devuelve un objeto Item.

    Es necesario convertir la segunda y tercera propiedad a int.

    Argumentos:
    item = ['Elixir of the Mongoose', ' 5', ' 7']
    """

    argumentos = []

    for propiedad in item:
        try:
            argumentos.append(int(propiedad.lstrip()))
            assert isinstance(argumentos[-1], int)
        except AssertionError:
            print("la propiedad %s ha de ser integer" % propiedad)
        except ValueError:
            argumentos.append(propiedad)

    return Item(*argumentos)


def test(tienda, estadoInventario):

    numeroPropiedadesItem = 3
    nombrePropiedadesItem = ["name", "sell_in", "quality"]

    for (offset, item) in enumerate(tienda.items):
        print(item)
        for i in range(1, numeroPropiedadesItem):
            propiedad = nombrePropiedadesItem[i]
            try:
                valorPropiedadCasoTest = int(estadoInventario[offset][i])
            except:
                valorPropiedadCasoTest = estadoInventario[offset][i]
            else:
                assert getattr(item, propiedad) == valorPropiedadCasoTest, \
                        "falla %s %s" % (propiedad, estadoInventario[offset][i])


if __name__ == "__main__":

    rutaAccesoFichero = "stdout.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    items = extraerItemsIventario(matrizCasosTest)

    inventario = []
    for item in items:
        objetoItem = crearObjetoItem(item)
        assert isinstance(objetoItem.sell_in, int)
        assert isinstance(objetoItem.quality, int)
        inventario.append(objetoItem)

    tienda = GildedRose(inventario)

    for dia in range(1, len(matrizCasosTest)):
        print('\n' + '#' * 5 + " Items en la tienda DIA %d " % dia + '#' * 5 + '\n')
        tienda.update_quality()
        estadoInventario = matrizCasosTest[dia]
        test(tienda, estadoInventario)
