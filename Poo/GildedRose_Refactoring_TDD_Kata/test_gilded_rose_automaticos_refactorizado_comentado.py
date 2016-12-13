
from gilded_rose_refactorizado import *
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
    # Construimos los argumentos del objeto.
    # Son necesarios, no podemos invocar Item()
    # name es la primera propiedad y el primer elemento
    # en la lista item.

    # argumentos.append(item[0])

    for propiedad in item:
        try:
            argumentos.append(int(propiedad.lstrip()))
            assert isinstance(argumentos[-1], int)
        except AssertionError:
            print("la propiedad %s ha de ser integer" % propiedad)
        except ValueError:
            argumentos.append(propiedad)

        """
        if propiedad.isdecimal():  <= falla para valores negativos
            print("true")
            argumentos.append(int(propiedad))
        else:
            print("false")
            argumentos.append(propiedad)
        """

        # str.strip([chars])
        # Return a copy of the string with the leading and trailing characters removed.
        # The chars argument is a string specifying the set of characters to be removed.
        # If omitted or None, the chars argument defaults to removing whitespace.
        # sell_in = " 6" => existe un espacio en blanco antes del numero,
        # lo extraemos y convertimos a entero
        # argumentos.append(int(propiedad.strip()))

    # chequeo que sell_in y quality son enteros
    # for arg in argumentos[1:]: <= esto es incorrecto sin el assert
    #    assert isinstance(arg, int)

    # creo el objeto y lo devuelvo
    diccionarioClases = {"Sulfuras, Hand of Ragnaros": "Sulfuras",
                         "Aged Brie": "AgedBrie",
                         "Backstage passes to a TAFKAL80ETC concert": "Backstage",
                         "Conjured Mana Cake": "ConjuredItem",
                         "+5 Dexterity Vest": "ConjuredItem",
                         "Normal Item": "NormalItem"}
    try:
        clase = diccionarioClases[item[0]]
    except KeyError:
        clase = diccionarioClases["Normal Item"]
    finally:
        return eval(clase + str(tuple(argumentos)))
    # return Item(*argumentos)

    '''
    keysDiccionarioItem = ["name", "sell_in", "quality"]

    # he de pasar argumentos al constructor obligatoriamente

    objetoItem = Item("name", "sell_In", "quality")

    for (offset, propiedad) in enumerate(keysDiccionarioItem):
            objetoItem.__dict__[propiedad] = item[offset]

    return objetoItem
    '''


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
                assert getattr(item, propiedad) == valorPropiedadCasoTest, "falla %s %s %s" % (propiedad, estadoInventario[offset][i], item.__class__.__name__)


if __name__ == "__main__":

    # rutaAccesoFichero = "stdout.gr"
    rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []

    # Cargar los casos test del fichero de texto
    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    # Averiguar que items habra en el inventario  de la tienda
    items = extraerItemsIventario(matrizCasosTest)
    # items = [ [], [], [], ... ]

    # Crear los objetos que componen el inventario
    inventario = []
    for item in items:
        objetoItem = crearObjetoItem(item)
        assert isinstance(objetoItem.sell_in, int)
        assert isinstance(objetoItem.quality, int)
        inventario.append(objetoItem)

    # Inicializar /crear la tienda con el inventario
    tienda = GildedRose(inventario)

    """
    print('\n' + '#' * 5 + "Items en la tienda DIA 1: " + '#' * 5 + '\n')
    for item in tienda.items:
        print(item)

    tienda.update_quality()

    print('\n' + '#' * 5 + "Items en la tienda DIA 2: " + '#' * 5 + '\n')
    for item in tienda.items:
        print(item)
    """

    # Comparar el resultado del dia con el caso test de ese dia

    for dia in range(1, len(matrizCasosTest)):
        print('\n' + '#' * 5 + " Items en la tienda DIA %d " % dia + '#' * 5 + '\n')
        tienda.update_quality()
        estadoInventario = matrizCasosTest[dia]
        test(tienda, estadoInventario)
