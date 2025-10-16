from collections import defaultdict
from typing import List

class Solution():
    def validPath(self, n: int, edges: List[List[int]], source:int, destination:int):
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(curr_node):
            if curr_node == destination:
                return True
            seen[curr_node] = True
            for next_node in graph(curr_node):
                if not seen[curr_node]:
                    if dfs(next_node): # in this case its more like if True then return True
                        return True
            return False

        return dfs(source)


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

