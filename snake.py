import random


class Snake:
    active = 0
    started = 0
    width = 0
    size = 0
    fiiledSize = 0

    def __init__(self, size):
        self.size = size
        self.snake = [' '] * size

    def start(self):
        self.started = 1
        self.active = 1

    def go(self):
        if self.started == 0:
            return

        if self.active:
            if self.width == 8:
                if self.fiiledSize == self.size:
                    self.width = 0
                    self.active = 0
                else:
                    del self.snake[-1]
                    self.snake.insert(0, ' ')
                    self.fiiledSize += 1
            else:
                del self.snake[-1]
                self.snake.insert(0, self.rand())
                self.width += 1
                self.fiiledSize += 1
        else:
            if self.fiiledSize != 1:
                del self.snake[-1]
                self.snake.insert(0, ' ')

                self.fiiledSize -= 1
            else:
                self.active = 1

    def rand(self):
        return ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5'][random.randint(0, 9)]

    def __str__(self):
        out = ''
        for i in self.snake:
            out += i

        return out
