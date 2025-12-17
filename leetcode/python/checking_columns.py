# this task it to store columns and rows in two separate dics
from collections import defaultdict



def get_col_and_row(grid):
    def convert_to_key(arr):
        return tuple(arr)

    kolumny = defaultdict(int)
    for col in range(len(grid[0])):
        current_col = []
        for row in range(len(grid)):
            current_col.append(grid[row][col])

        kolumny[convert_to_key(current_col)] += 1
    return kolumny




grid = [
  [10, 20],  # wiersz 0
  [30, 40]   # wiersz 1
]

print(get_col_and_row(grid))

