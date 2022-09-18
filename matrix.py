import terminal as TPut
from time import sleep
from snake import Snake
import random


class Matrix:
    cols = 0
    rows = 0
    matrix = []
    notActivedSkakes = []

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

        self.init()

    def init(self):
        self.matrix = [Snake(self.rows) for i in range(self.cols)]
        self.notActivedSkakes = len(self.matrix) - 1

    def go(self):
        self.loop()

    def loop(self):
        while True:
            sleep(0.02)

            if self.notActivedSkakes:
                choice = random.randint(0, self.notActivedSkakes)
                self.matrix[choice - 1].start()
                self.notActivedSkakes -= 1

            for snake in self.matrix:
                snake.go()
            # print(len(self.matrix))
            #
            TPut.clear()
            print(self)

    def __str__(self):
        out = ''
        for row in range( self.rows):
            for col in range(self.cols):
                # print()
                # print(len(str(self.matrix[col])))
                out += str(self.matrix[col])[row]
            out += "\n"

        return out


if __name__ == '__main__':
    print('This not is executable script')
