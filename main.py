import matrix as mt
from os import popen


def get_config_data():
    cols = popen('tput cols', 'r').read()
    rows = popen('tput lines', 'r').read()

    return {
        'cols': cols,
        'rows': rows
    }
def go_matrix():
    config = get_config_data()

    matrix = mt.Matrix(rows=config.rows, cols=config.cols)

    matrix.go()


if __name__ == '__main__':
    go_matrix()
