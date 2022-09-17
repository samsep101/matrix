import terminal as TPut
from time import sleep
import char


class Matrix:
    cols = 0
    rows = 0
    matrix = []

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

        self.init()

    def init(self):
        self.matrix = [[''] * self.cols] * self.rows

    def go(self):
        self.loop()

    def loop(self):
        while True:
            sleep(0.3)
            TPut.clear()
            self.matrix.pop(self.rows - 1)
            self.matrix.insert(0, [char.Char() for i in range(0, self.cols)])
            print(self)


    def __str__(self):
        out = ''
        for rows in self.matrix:
            out += "\n"
            for line in rows:
                out += str(line)

        return out


if __name__ == '__main__':
    print('This not is executable script')
