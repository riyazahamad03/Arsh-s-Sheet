class solution:
    def __init__(self, n: int):
        self.n = n
        self.color = [0] * (n)

    def isSafe(self, node, adj, col):
        for n in adj[node]:
            if self.color[n] == col:
                return False
        return True

    def mapColouring(self, adj: list[list[int]], m: int):
        def dfs(node):
            if node == self.n:
                return True

            for c in range(m):
                if self.isSafe(node, adj, c):
                    self.color[node] = c

                    if dfs(node + 1):
                        return True
                    self.color[node] = 0

            return False
        return dfs(0)


x = solution(4)
print(x.mapColouring([[1, 2, 3], [0, 2, 3], [0, 1], [1, 0]], 3))
