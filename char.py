import random

charters = [
    'a', 'b', 'c', ' ', 'd', 'e', '1', '2', '3', '4', '5', ' '
]

class Char:
    def __init__(self):
        self.char = charters[random.randint(0, len(charters) - 1)]

    def __str__(self):
        return self.char


if __name__ == '__main__':
    print('This not is executable script')