#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
# Author mahamdi amine                                    #
# Github https://github.com/MahamdiAmine                  #
###########################################################


# NumPy is a library for the Python programming language, adding support for large,
# multi-dimensional arrays and matrices, along with a large collection of high-level mathematical
# functions to operate on these arrays.
import numpy as np


class Knapsac:

# the knapSac function takes the n objects and returns the matrix of the max values
    def knapSack(max_weight, weight, value):
        #Apply the definition(recursive equations )
        n = len(value)
        matrix = [[0 for x in range(max_weight + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for w in range(max_weight + 1):
                if i == 0 or w == 0:
                    matrix[i][w] = 0
                elif weight[i - 1] <= w:
                    matrix[i][w] = max(value[i - 1] + matrix[i - 1][w - weight[i - 1]], matrix[i - 1][w])
                else:
                    matrix[i][w] = matrix[i - 1][w]
        return matrix


# checking to see which items will go into our knapsack
    def check_items(weight, matrix, max_weight):
        col = max_weight
        packed = []
        for i in range(len(weight) - 1, -1, -1):
            if i == 0 and matrix[i][col] != 0:
                packed.insert(0, i)
            if matrix[i][col] != matrix[i - 1][col]:
                packed.insert(0, i)
                col -= weight[i]
        packed = np.unique(packed)  #do not pack double items
        return packed

