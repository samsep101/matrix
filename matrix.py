class Matrix:
    cols = 0
    rows = 0
    matrix = []

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

        self.init()

    def init(self):
        self.matrix = [
            ['0'] * self.rows
        ] * self.cols

    def go(self):
        pass

    def __str__(self):
        print('matrix')


if __name__ == '__main__':
    print('This not is executable script')
