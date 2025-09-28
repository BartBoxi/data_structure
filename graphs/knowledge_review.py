from collections import defaultdict

def createGraph(edges):
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
    return graph

n = 4
edges = [[0, 1], [0, 2], [1, 3]]

print(createGraph(n, edges))
