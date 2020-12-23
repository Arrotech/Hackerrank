import math
import os
import random
import re
import sys


def hourglassSum(arr):

    def hour_glass_sum(arr, i, j):
        sum_h = 0
        sum_h += arr[i-1][j-1]
        sum_h += arr[i-1][j]
        sum_h += arr[i-1][j+1]
        sum_h += arr[i][j]
        sum_h += arr[i+1][j-1]
        sum_h += arr[i+1][j]
        sum_h += arr[i+1][j+1]

        return sum_h

    res = []
    for i in range(1, 5):
        for j in range(1, 5):
            curr_sum = hour_glass_sum(arr, i, j)
            res.append(curr_sum)
    print(max(res))


arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0,  0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print(hourglassSum(arr))
