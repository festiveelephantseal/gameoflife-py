#!/usr/bin/python3

"""
Game of life implementation in python
"""

import random
import time
import argparse


def initboard(rows, columns):
    board = []
    for i in range(0, rows):
        board.append([])

    for i in board:
        for _ in range(0, columns):
            i.append(round(random.random()))
    return board


def printboard(board):
    for x in board:
        string = ""
        for y in x:
            if y == 1:
                string += "X"
            else:
                string += " "
        print(string)


def nextboard(board):
    nextgeneration = board.copy()

    # Calculate amount of neighbors
    for i in range(0, len(nextgeneration)-1):
        for j in range(0, i):
            neighbors = [nextgeneration[i-1][j-1], nextgeneration[i-1][j], nextgeneration[i-1][j+1], nextgeneration[i]
                         [j-1], nextgeneration[i][j+1], nextgeneration[i+1][j-1], nextgeneration[i+1][j], nextgeneration[i+1][j+1]]

            aliveneighbors = 0

            for neighbor in neighbors:
                if neighbor == 1:
                    aliveneighbors += 1
            if nextgeneration[i][j] == 1:
                if (aliveneighbors < 2) or (aliveneighbors > 3):
                    nextgeneration[i][j] = 0
            else:
                if aliveneighbors == 3:
                    nextgeneration[i][j] = 1

    return nextgeneration


def main():
    parser = argparse.ArgumentParser(description="Conways Game of Life")
    parser.add_argument("--rows", dest="rows", required=True)
    parser.add_argument("--columns", dest="cols", required=True)
    args = parser.parse_args()

    board = initboard(int(args.rows), int(args.cols))

    while True:
        time.sleep(1)

        nextgen = nextboard(board)

        print("---New Gen---")

        printboard(nextgen)

if __name__ == '__main__':
    main()