from collections import defaultdict, deque

# n = 3 (nodes are 0, 1, 2)
#
# edges = [[0, 1], [1, 2]]
#
# source = 0
#
# destination = 2

def has_path(n, edges, source, destination):
    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([source])
    visited = {source}

    while queue:
        current_node = queue.popleft()
        if current_node == destination:
            return True
        else:
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    return False



n = 3
edges = [[0, 1], [1, 2]]
source = 0
destination = 2
print(has_path(n,edges,source, destination))

