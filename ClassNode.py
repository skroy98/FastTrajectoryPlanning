import random
import math
import heapq
import sys
import time
import timeit
import matplotlib as mpl
from matplotlib import pyplot
import numpy as np


height = 101
width = 101
reverse = False
adaptive = False


class Node:
    def __init__(self, value, i, j):
        self.value = value
        self.i = i  # x index
        self.j = j  # y index
        # self.g = 0  # cost
        self.g = math.inf
        self.h = 0  # heuristic value
        self.f = math.inf  # total g+h
        self.neighbors = []
        self.prev = None
        self.adjust = False

# # uncomment for lower G tie-breaking
#    def __lt__(self, other):  # lower g tie breaking
#        return self.g < other.g

## setting to higher G by default. Comment below function for lower G
    def __gt__(self, other):  # higher g tie breaking
        return self.g < other.g



    def find_neighbors(self, grid):
        i = self.i
        j = self.j
        if (i-1) > -1 and (i - 1) < width:
            self.neighbors.append(grid[i-1][j])
        if (j-1) > -1 and (j-1) < height:
            self.neighbors.append(grid[i][j-1])
        if (i+1) < width:
            self.neighbors.append(grid[i+1][j])
        if (j+1) < height:
            self.neighbors.append(grid[i][j+1])


# heuristic function
def heuristic(a, b):
    d = abs(a.i - b.i) + abs(a.j - b.j)
    return d


def createGrid(grid, width, height):
    cols = []
    rows = []

    for i in range(width):
        for j in range(height):
            rows.append(Node(grid[i][j], i, j))
        cols.append(rows)
        rows = []
    return cols


def loadNeighbors(grid, width, height):
    for i in range(width):
        for j in range(height):
            grid[i][j].find_neighbors(grid)
    return grid


def printGrid(grid, width, height):
    for i in range(width):
        for j in range(height):
            print(grid[i][j].value, end=' ')
        print()
    return


def updateGrid(grid, pathSet):
    for i in range(len(pathSet)):
        x = pathSet[i].i
        y = pathSet[i].j
        grid[x][y].value = 8

