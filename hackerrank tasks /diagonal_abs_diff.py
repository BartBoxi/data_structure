import math
import os
import random
import re
import sys

def countabsdiff(arr):
    right = 0
    left = 0
    n = len(arr)
    for i in range(n):
        column_right = (n - 1) - i
        val_left = arr[i][i]
        left += val_left
        val_right = arr[i][column_right]
        right += val_right

    return abs(right - left)

arr = [[-1, 1, -7, -8],
       [-10, -8, -5, -2],
       [0, 9, 7, -1],
       [4, 4, -2, 1]]

print(countabsdiff(arr))



