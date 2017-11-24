import matplotlib.pyplot as plt
from random import shuffle


def createRandomList(length):
    # recibe como parametro la longitud de la lista
    # crea una lista de numero enteros
    # la "mezcla" = desordena
    # devuelve la lista


def display(lista):
    plt.clf()
    plt.bar(range(len(lista)), lista)
    plt.draw()


def less(a, b):
    # comprueba si a es menor que b
    # devuelve un boolean
    # recibe dos elementos
    # ojo a si el algoritmo de ordenacion es estable o inestable


def exchange(lista, i, j):
    # intercambia dos elementos de posicion en la lista
    # recibe la lista, la posicion i y la posicion j
    # devuelve None
    # comprueba que se han intercambiado los elementos


def isExchanged(lista, i, j):
    # comprueba si el elemento en la posicion i
    # es menor que el elemento en la posicion j
    # devuelve un boolean


def isSorted(lista):
    # comprueba si la lista esta oredenada
    # devuelve un boolean


def bubbleSort(lista):
    # ordena la lista segun el algoritmo de ordenacion
    # bubble sort
    # cada vez que se intercambian dos elementos se dibuja la lista:
    # llama a display(lista)
    # devuelve None
    # Comprueba que la lista esta ordenada


if __name__ == "__main__":

    plt.ion()
    lista = createRandomList(15)
    bubbleSort(lista)
    isSorted(lista)
    plt.show(block=True)

    # Listas de strings como casos test #
    # desactivar display() en bubbleSort()

    for test in open("stringTestCases.txt", 'r'):
        testList = list(test.replace(' ', ''))
        bubbleSort(testList)
        assert isSorted(testList), "Test %s " % (str(test))

    print("string test cases passed")
