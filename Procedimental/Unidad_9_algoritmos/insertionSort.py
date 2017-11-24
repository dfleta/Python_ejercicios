
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


def isSorted(lista):
    for (offset, element) in enumerate(lista[:-1]):
        if element > lista[offset + 1]:
            return False
    return True


def isExchanged(lista, i, j):
    if less(lista[i], lista[j]):
        return True
    return False


def insertionSort(lista):
    for j in range(1, len(lista)):
        i = j - 1
        while i >= 0:
            if less(lista[j], lista[i]):
                exchange(lista, i, j)
                j -= 1
                # display(lista)
            else:
                break
            i -= 1
    assert isSorted(lista)
    return lista


if __name__ == "__main__":

    # list of integer test case #

    plt.ion()
    lista = createRandomList(10)
    insertionSort(lista)
    plt.show(block=True)

    # Lists of string test cases #
    # turn off display()

    for test in open("stringTestCases.txt", 'r'):
        testList = list(test.replace(' ', ''))
        insertionSort(testList)
        assert isSorted(testList), "Test %s " % (str(test))

    print("string test cases passed")
