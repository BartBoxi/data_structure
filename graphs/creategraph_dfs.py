from collections import defaultdict
def getGraph(n,edges,source, destination):
    stack = [source]
    visited = {source}
    graph = {}

    for u,v in edges:
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)
        if v not in graph:
            graph[v] = [u]
        else:
            graph[v].append(u)

    while stack:
        current_node = stack.pop()
        if current_node == destination:
            return True
        else:
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    return False


n=4
edges = [[0,1], [0,2],[1,0] , [1,3], [2,0], [3,1]]

source = 0

destination = 3


print(getGraph(n,edges, source, destination))