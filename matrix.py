import terminal as TPut


class Matrix:
    cols = 0
    rows = 0
    matrix = []

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

        self.init()

    def init(self):
        TPut.clear()
        self.matrix = [[''] * self.cols] * self.rows

    def go(self):
        print(self)

    def __str__(self):
        out = ''
        for rows in self.matrix:
            out += "\n"
            for line in rows:
                out += line

        return out


if __name__ == '__main__':
    print('This not is executable script')
