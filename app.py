import logging
import numpy
from flask import Flask, render_template, request

from business.sudoku import solve
from clients.template_client import get_sudoku

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route('/', methods=['GET', 'POST'])
def process_sudoku():
    if request.method == 'GET':
        return render_template('grille.html.jinja2')
    else:
        result = request.form
        if "fetch" in request.form:
            tab = get_sudoku(3)
            return render_template('grille.html.jinja2', old=tab)
        else:
            tab = numpy.zeros((9, 9), dtype=int)
            for key, value in result.items():
                if key != "type" and value != "":
                    i = int(key[0])
                    j = int(key[1])
                    tab[i, j] = int(value)
            res = solve(tab)
            return render_template('grille.html.jinja2', old=tab, new=res)


if __name__ == '__main__':
    app.run()
