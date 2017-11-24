
import matplotlib.pyplot as plt
from random import shuffle


def createRandomList(length):
    lista = [number for number in range(length)]
    shuffle(lista)
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


def shellSort(lista):
    gaps = []
    N = len(lista)
    h = 1
    k = 1
    while h <= N / 3:
        gaps.insert(0, h)
        k += 1
        h = (3**k - 1) // 2

    assert gaps[0] <= N / 3

    # escribir el bucle de dentro a fuera: code complete
    for gap in gaps:
        j = gap
        while j < N:
            i = j - gap
            while i >= 0:
                if less(lista[i + gap], lista[i]):
                    exchange(lista, i, i + gap)
                    # display(lista)
                i -= gap
            j += 1
    assert isSorted(lista)
    return lista


if __name__ == "__main__":

    # list of integer test case #

    plt.ion()
    lista = createRandomList(20)
    shellSort(lista)
    plt.show(block=True)

    # Lists of string test cases #
    # turn off display()

    for test in open("stringTestCases.txt", 'r'):
        characterList = list(test.replace(' ', ''))
        shellSort(characterList)
        assert isSorted(characterList), "Test %s " % (str(test))

    print("string test cases passed")
