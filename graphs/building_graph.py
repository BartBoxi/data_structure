# i have a graph as visualization represtation 
# i need to build the input for that data 
# edges = [[0, 1], [1, 2], [2, 0], [2, 3]].

from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)
    
    for x, y in edges:
        graph[x].append(y)
    return graph


edges = [[0, 1], [1, 2], [2, 0], [2, 3]]
print(build_graph(edges))


