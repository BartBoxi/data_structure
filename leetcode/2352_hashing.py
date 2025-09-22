from collections import defaultdict
from typing import List

def equalPairs(grid: List[List[int]])-> int:
    def convert_to_key(arr):
        return tuple(arr)

    dic = defaultdict(int)
    for row in grid:
        dic[convert_to_key(row)] += 1

    dic2 = defaultdict(int)
    for col in range(len(grid[0])): ### for col in range(len([1,2,3])) --> 3
                                    # how many items in first row
        current_col = []
        for row in range(len(grid)): ## tutaj tez jakby jest 3 # how many rows
            current_col.append(grid[row][col])

        dic2[convert_to_key(current_col)] += 1
    ans = 0
    for arr in dic:
        ans = dic[arr] * dic2[arr]
    return ans


grid = [
  [10, 20, 30],  # wiersz 0
  [30, 40]   # wiersz 1
]

print(equalPairs(grid))





