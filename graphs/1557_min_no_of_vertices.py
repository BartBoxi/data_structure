import collections
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n:int, edges: list[List[int]]) -> List[int]:
        incoming = collections.defaultdict(list)
        for src, dst in edges:
            incoming[dst].append(src)
        print(incoming)


        res = []
        for i in range(n):
            if not incoming[i]:
                res.append(i)
        return res

n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
solver = Solution()
print(solver.findSmallestSetOfVertices(n, edges))