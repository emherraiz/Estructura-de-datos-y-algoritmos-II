#!/bin/python3

import math
import os
import random
import re
import sys

fptr = open(os.environ['OUTPUT_PATH'], 'w')

class Matrix:
    _n = 0
    _m = 0
    elementos = None
    def __init__(self, n, m):
        self._n = n
        self._m = m
        self.elementos = []
        for i in range(self._n):
            self.elementos.append([])
            for j in range(self._m):
                self.elementos[i].append(0)

    def define_element(self, i, j, v):
        self.elementos[i][j] = v

    def show_matrix(self):
        for i in range(self._n):
            for j in range(self._m):
                # Imprime de una forma elegante la matriz
                print("| {0} ".format(self.get_value_of_position(i, j)), sep=',', end='')
            print('|\n')

    # def simpleArraySum(self, ar):
    #     for i in range(len(ar)):

mf = Matrix(3,5)

""" if __name__ == '__main__':
fptr = open(os.environ['OUTPUT_PATH'], 'w')
ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = simpleArraySum(ar)
fptr.write(str(result) + '\n')
fptr.close() """
