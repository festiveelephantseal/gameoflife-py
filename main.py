#!/usr/bin/python3

"""
Game of life implementation in python
"""

import random

board = []


def initboard(board: list, rows, columns):
    for i in range(0, rows):
        board.append([])

    for i in board:
        for _ in range(0, columns):
            i.append(round(random.random()))


def printboard(board: list):
    for x in board:
        string = ""
        for y in x:
            if y == 1:
                string += "X"
            else:
                string += " "
        print(string)


def nextboard(board: list, x, y):
    pass


initboard(board, 10, 10)

printboard(board)
