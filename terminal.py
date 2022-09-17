from os import popen
from os import system


def sys(command):
    return popen('tput ' + command, 'r').read()


def cols():
    return sys('cols')


def rows():
    return sys('lines')


def clear():
    return system('reset')


