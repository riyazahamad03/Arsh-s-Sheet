class solution:
    def isCyclic(self, v, adj):
        WHITE = 0
        GRAY = 1
        BLACK = 2

        color = [WHITE] * v

        def dfs(node):
            if color[node] == GRAY:
                return True
            if color[node] == BLACK:
                return False

            color[node] = GRAY
            for n in adj[node]:
                if dfs(n):
                    return True
            color[node] = BLACK
            return False

        for i in range(v):
            if dfs(i):
                return 1
        return 0


x = solution()
print(x.isCyclic(4, [[1], [2], [3], [3]]))
