class solution:
    def __init__(self, n):
        self.n = n
        self.color = [0] * (n)

    def mColoring(self, m, e, edges):
        def isSafe(node, col):
            for i in range(self.n):
                if (i != node and ((edges[i][0] == node and self.color[i] == col) or
                                   (edges[i][1] == node and self.color[i] == col))):

                    return False
        return True

        def dfs(node):
            if node == self.n:
                return True
            for idx in range(1, self.n + 1):
                if isSafe(node, idx):
                    self.color[node] = idx
                    if dfs(node + 1):
                        return True
                    self.color[node] = 0
            return False
        return dfs(0)


x = solution(4)
print(x.mColoring(3, 5, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]))
