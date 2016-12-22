
from gilded_rose_refactorizado import *
from accesoCasosTexttest_deudatecnica_saneada import *


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
    Devuelve un objeto de la clase Item.

    Es necesario convertir la segunda y tercera propiedad a int.

    Argumentos:
    item = ['Elixir of the Mongoose', ' 5', ' 7']
    """
    diccionarioClases = {"Sulfuras, Hand of Ragnaros": "Sulfuras",
                         "Aged Brie": "AgedBrie",
                         "Backstage passes to a TAFKAL80ETC concert": "Backstage",
                         "Conjured Mana Cake": "ConjuredItem",
                         "+5 Dexterity Vest": "ConjuredItem",
                         "Normal Item": "NormalItem"}

    try:
        nombreItem = item[0]
        clase = diccionarioClases[nombreItem]
    except KeyError:
        clase = diccionarioClases["Normal Item"]
    finally:
        return eval(clase + str(tuple(item)))


def test(tienda, estadoInventario):

    nombrePropiedadesItem = ["name", "sell_in", "quality"]
    numeroPropiedadesItem = len(nombrePropiedadesItem)

    for (offset, item) in enumerate(tienda.items):
        print(item)
        for i in range(1, numeroPropiedadesItem):
            propiedad = nombrePropiedadesItem[i]
            valorPropiedadCasoTest = estadoInventario[offset][i]
            assert getattr(item, propiedad) == valorPropiedadCasoTest, \
                "falla %s %s %s" % (propiedad, estadoInventario[offset][i], item.__class__.__name__)


if __name__ == "__main__":

    rutaAccesoFichero = "stdout_bug_conjured.gr"

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
