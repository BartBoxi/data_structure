from typing import List

def numIslands(grid:List[List[str]]) -> int:
    def valid(row, col):
        ### m and n are grid dimensions like grid m X n
        return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

    def dfs(row,col):
        for dx, dy in directions:
            next_row, next_col = row + dy, col + dy


### TODO: Finish the rest of the code from Leetcode and analyze it
