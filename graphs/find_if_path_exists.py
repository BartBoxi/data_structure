from typing import List

from collections import deque
from collections import defaultdict

### BFS Solution
class Solution():
    def findifthepathexists(self, n:int, edges:List[List[int]], source:int, destination:int):
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # storing all the nodes to be visited in the queue
        seen = [False] * n
        seen[source] = True
        queue = deque([source])
        print(seen)
        print(seen[source])

        while queue:
            current_node = queue.popleft()
            if current_node == destination:
                return True
            import collections
            from typing import List

            from collections import deque, defaultdict

            ### BFS Solution
            class Solution():
                def findifthepathexists(self, n: int, edges: List[List[int]], source: int, destination: int):
                    graph = collections.defaultdict(list)
                    for a, b in edges:
                        graph[a].append(b)
                        graph[b].append(a)

                    # storing all the nodes to be visited in the queue
                    seen = [False] * n
                    seen[source] = True
                    queue = collections.deque([source])
                    print(seen)
                    print(seen[source])

                    while queue:
                        current_node = queue.popleft()
                        if current_node == destination:
                            return True

                        for next_node in graph[current_node]:
                            if not seen[next_node]:
                                seen[next_node] = True
                                queue.append(next_node)
                        return False

            edges = [[0, 1], [1, 2], [2, 0]]
            n = 3
            source = 0
            destination = 2

            solution = Solution()
            print(solution.findifthepathexists(n, edges, source, destination))

            for next_node in graph[current_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)
            return False


edges = [[0,1],[1,2],[2,0]]
n = 3
source = 0
destination = 2


solution = Solution()
print(solution.findifthepathexists(n, edges, source, destination))


