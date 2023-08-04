import collections


class Graph:
    def __init__(self, Vertices):
        self.v = Vertices
        self.graph = collections.defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    def transpose(self):
        g = Graph(self.v)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def kosaraju(self):
        visited = [False] * (self.v)
        stack = []

        for i in range(self.v):
            if not visited[i]:
                self.dfs(i, visited, stack)
        transposedGraph = self.transpose()
        visited = [False] * (self.v)
        connList = []

        while stack:
            idx = stack.pop()
            if not visited[idx]:
                scc = []
                transposedGraph.dfs(idx, visited, scc)
                connList.append(scc)
        return connList


g = Graph(5)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(1, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)


listElem = g.kosaraju()
for it in listElem:
    print(it)
