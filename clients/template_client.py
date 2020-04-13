import requests
import numpy
from decorators.execution_time import execution_time


@execution_time
def get_sudoku(difficulty):
    response = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level=' + str(difficulty))
    data = response.json()
    tab = numpy.zeros((9, 9), dtype=int)
    for square in data["squares"]:
        tab[square["x"], square["y"]] = square["value"]
    return tab
