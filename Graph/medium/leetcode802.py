class solution:
    def eventualSafeNode(self, graph: list[list[int]]):
        safeState = {}

        def dfs(node):
            if node in safeState:
                return safeState[node]
            safeState[node] = False
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            safeState[node] = True
            return True
        res = []
        for n in range(len(graph)):
            if dfs(n):
                res.append(n)
        return res


x = solution()
print(x.eventualSafeNode([[1, 2], [2, 3], [5], [0], [5], [], []]))
