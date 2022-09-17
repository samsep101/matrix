import matrix as mt
import terminal as TPut


def get_config_data():
    cols = TPut.cols()
    rows = TPut.rows()

    return {
        'cols': int(cols),
        'rows': int(rows)
    }


def go_matrix():
    config = get_config_data()

    matrix = mt.Matrix(rows=config['rows'], cols=config['cols'])

    matrix.go()


if __name__ == '__main__':
    go_matrix()
