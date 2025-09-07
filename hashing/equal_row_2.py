from collections import defaultdict
from typing import List


def equalPairs(grid:List[List[int]])-> int:
    def convert_to_key(arr):
        return tuple(arr)

    ### Counting rows
    row_counts = defaultdict(int)
    for row in grid:
        row_tuple = tuple(row)
        row_counts[row_tuple] +=1

    ### counting columns
    col_counts = defaultdict(int)
    n = len(grid)
    for col in range(n):
        current_col = []
        for row in range(n):
            current_col.append(grid[row][col])

        col_counts[convert_to_key(current_col)] += 1

    ans = 0
    for arr in row_counts:
        ans += row_counts[arr] * col_counts[arr]

    return ans





