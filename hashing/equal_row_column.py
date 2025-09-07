from collections import defaultdict
from typing import List

def equalPairs(grid:List[List[int]]) -> int:
    def convert_to_key(arr):
        return tuple(arr)


    ### this code is describing how many diff rows we have
    dic = defaultdict(int)
    #print(grid)
    for row in grid:
        dic[convert_to_key(row)] += 1 # here we count how many times each row appeared in the dic
        #print(f"this is {dic}")

    #print(f"this is grid 0{grid[0]}")

    ###

    dic2 = defaultdict(int)
    for col in range(len(grid[0])):
        currentcol = []
        for row in range(len(grid)):
            currentcol.append(grid[row][col]) ## to buduje grida od nowa, ale po co?
        dic2[convert_to_key(currentcol)] += 1

    ans = 0
    for arr in dic:
        ans += dic[arr] * dic2[arr]

    return ans

grid = [[3,2,1],[1,7,6],[2,7,7]]

print(equalPairs(grid))