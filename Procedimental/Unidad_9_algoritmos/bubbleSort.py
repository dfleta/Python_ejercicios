import matplotlib.pyplot as plt
from random import shuffle


def createRandomList(length):
    lista = [number for number in range(length)]
    # shuffle no devuelve nada: cambia la lista in place
    # porque las listas son objetos mutables
    shuffle(lista)
    assert len(lista) == length
    return lista


def display(lista):
    plt.clf()
    plt.bar(range(len(lista)), lista)
    plt.draw()


def less(a, b):
    return a < b


def exchange(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]
    assert isExchanged(lista, i, j)


def isExchanged(lista, i, j):
    if less(lista[i], lista[j]):
        return True
    return False


def isSorted(lista):
    for (offset, element) in enumerate(lista[:-1]):
        if element > lista[offset + 1]:
            return False
    return True


def bubbleSort(lista):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lista) - 1):
            if less(lista[i + 1], lista[i]):
                exchange(lista, i, i + 1)
                # comentar esta linea para pasar los casos test con string
                # display(lista)
                swapped = True
    assert isSorted(lista)
    return lista


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
