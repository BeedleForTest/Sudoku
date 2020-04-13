import numpy

from decorators.execution_time import execution_time


def is_possible(value, x, y, array):
    for i in range(9):
        if value == array[i, y] or value == array[x, i]:
            return False
    inf_x = int(x // 3) * 3
    inf_y = int(y // 3) * 3
    for i in range(inf_x, inf_x + 3):
        for j in range(inf_y, inf_y + 3):
            if value == array[i, j]:
                return False
    return True


def rec_solve(array):
    for y in range(9):
        for x in range(9):
            if array[x, y] == 0:
                for value in range(1, 10):
                    if is_possible(value, x, y, array):
                        array[x, y] = value
                        resolved, solution = rec_solve(array)
                        if resolved:
                            return True, solution
                        array[x, y] = 0
                return False, array
    return True, array


@execution_time
def solve(array):
    solved, solution = rec_solve(numpy.copy(array))
    return solution
