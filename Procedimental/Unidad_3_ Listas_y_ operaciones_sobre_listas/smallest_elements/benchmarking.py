
import time
from smallest_elements_comprehension import first_n_smallest as comprehension
from smallest_elements import first_n_smallest as modular
from smallest_elements_min import first_n_smallest as turing


def benchmark(func, *args):
    start_time = time.clock()
    func(*args)
    run_time = time.clock() - start_time
    return run_time


if __name__ == "__main__":

    print("\n### Caso test exhaustivo ###\n")

    print("Comprehension => " + str(benchmark(comprehension, [-3, -6, -7, 10, 4, -2, 8, -6, 10, 8, 10, -2, -5,
                                    0, 3, 4, 4, -6, 0, 1, 5, 1, 10,
                                    9, 6, -9, -8, 9, -2,
                                     -1, -1, 2, -7, 10, -10, -8,
                                    2, -10, -5, -3], 8)))


    print("Modular => " + str(benchmark(modular, [-3, -6, -7, 10, 4, -2, 8, -6, 10, 8, 10, -2, -5,
                             0, 3, 4, 4, -6, 0, 1, 5, 1, 10,
                             9, 6, -9, -8, 9, -2, -1, -1, 2, -7, 10, -10, -8,
                             2, -10, -5, -3], 8)))


    print("Turing => " + str(benchmark(turing, [-3, -6, -7, 10, 4, -2, 8, -6, 10, 8, 10, -2, -5,
                             0, 3, 4, 4, -6, 0, 1, 5, 1, 10,
                             9, 6, -9, -8, 9, -2, -1, -1, 2, -7, 10, -10, -8,
                             2, -10, -5, -3], 8)))


    print("\n### Caso test elementosTotal = 0 ###\n")

    print("Comprehension => " + str(benchmark(comprehension, [1, 2, 3, 4, 5], 0)))


    print("Modular => " + str(benchmark(modular, [1, 2, 3, 4, 5], 0)))


    print("Turing => " + str(benchmark(turing, [1, 2, 3, 4, 5], 0)))

    print("\n### Caso test [1, 2, 3, -4, 0], 3  ###\n")

    print("Comprehension => " + str(benchmark(comprehension, [1, 2, 3, -4, 0], 3)))

    print("Modular => " + str(benchmark(modular, [1, 2, 3, -4, 0], 3)))

    print("Turing => " + str(benchmark(turing, [1, 2, 3, 4, 5], 0)))

    '''
    assert first_n_smallest([], 3) == []
    assert first_n_smallest([1, 2, 3, 4, 5], 0) == []
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
    '''
