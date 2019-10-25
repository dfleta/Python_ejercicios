
def first_n_smallest(listaNumeros, elementosTotal):

    if elementosTotal == 0 or not listaNumeros:
        return []

    if elementosTotal == len(listaNumeros):
        return listaNumeros

    listaMenores = []
    maximo = 0
    for posicion, numero in enumerate(listaNumeros[:elementosTotal]):
        listaMenores.append(numero)
        if numero >= maximo:
            maximo = numero

    assert len(listaMenores) == elementosTotal

    for numero in listaNumeros[posicion + 1:]:
        if numero < maximo:
            listaMenores.append(numero)
            maximo = calcularMaximo(listaMenores[:])
            extraerUltimoMaximo(listaMenores, maximo)
            maximo = calcularMaximo(listaMenores[:])
            assert len(listaMenores) == elementosTotal

    return listaMenores


def calcularMaximo(lista):
    lista.sort()
    return lista[-1]


def extraerUltimoMaximo(lista, maximo):
    lista.reverse()
    # try - except necesario
    lista.remove(maximo)
    lista.reverse()


if __name__ == "__main__":

    assert first_n_smallest([1, 2, 3, 4, 5], 0) == []
    assert first_n_smallest([], 3) == []
    assert first_n_smallest([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert first_n_smallest([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    assert first_n_smallest([5, 4, 3, 2, 1], 3) == [3, 2, 1]
    assert first_n_smallest([1, 2, 3, 1, 2], 3) == [1, 2, 1]
    assert first_n_smallest([1, 2, 3, -4, 0], 3) == [1, -4, 0]
    assert first_n_smallest([1, 2, 3, 4, 2], 4) == [1, 2, 3, 2]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 2) == [2, 1]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 3) == [2, 1, 2]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 4) == [2, 1, 2, 2]

    # uno de los test exhaustivos
    assert first_n_smallest([-3, -6, -7, 10, 4, -2, 8, -6, 10, 8, 10, -2, -5,
                             0, 3, 4, 4, -6, 0, 1, 5, 1, 10,
                             9, 6, -9, -8, 9, -2, -1, -1, 2, -7, 10, -10, -8,
                             2, -10, -5, -3], 8) == \
        [-6, -7, -9, -8, -7, -10, -8, -10]
