from collections import defaultdict




# building the graph
def buildGraph(isConnected: list[list[int]]):
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
                #print(graph)
        print(graph)

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(buildGraph(isConnected))