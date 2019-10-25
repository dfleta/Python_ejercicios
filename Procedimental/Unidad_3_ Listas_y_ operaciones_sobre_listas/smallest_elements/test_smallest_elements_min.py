from smallest_elements_min import first_n_smallest


def test_devolver_ningun_elemento():
    assert first_n_smallest([1, 2, 3, 4, 5], 0) == []


def test_lista_numeros_vacia():
    assert first_n_smallest([], 3) == []


def test_devolver_todos_los_elementos():
    assert first_n_smallest([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]


def test_no_se_repiten_elementos():
    assert first_n_smallest([1, 2, 3, 4, 5], 3) == [1, 2, 3]


def test_no_se_repiten_elementos_minimo_decreciente():
    assert first_n_smallest([5, 4, 3, 2, 1], 3) == [3, 2, 1]


def test_elementos_repetidos_en_los_minimos():
    assert first_n_smallest([1, 2, 3, 1, 2], 3) == [1, 2, 1]


def test_elementos_negativos():
    assert first_n_smallest([1, 2, 3, -4, 0], 3) == [1, -4, 0]


def test_elementos_repetidos_no_entran_en_minimos_creciente():
    assert first_n_smallest([1, 2, 3, 4, 2], 4) == [1, 2, 3, 2]


def test_elementos_repetidos_no_entran_en_minimos_decreciente():
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 2) == [2, 1]


def test_elementos_repetidos_entran_en_minimos_decreciente():
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 3) == [2, 1, 2]


def test_elementos_repetidos_entran_en_minimos():
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 4) == [2, 1, 2, 2]


def test_eliminar_elemento_de_minimos_repetido_al_final():
    # uno de los test exhaustivos
    assert first_n_smallest([-3, -6, -7, 10, 4, -2, 8, -6, 10, 8, 10, -2, -5,
                             0, 3, 4, 4, -6, 0, 1, 5, 1, 10,
                             9, 6, -9, -8, 9, -2, -1, -1, 2, -7, 10, -10, -8,
                             2, -10, -5, -3], 8) == \
                                            [-6, -7, -9, -8, -7, -10, -8, -10]
