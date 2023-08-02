class solution:
    def dfs(self, graph: list[list[int]]):
        res = []
        visited = set()

        def dfs(node):
            visited.add(node)
            res.append(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)

        dfs(0)
        return res


x = solution()
print(x.dfs([[1, 2], [0, 2, 3], [0, 1], [1]]))
