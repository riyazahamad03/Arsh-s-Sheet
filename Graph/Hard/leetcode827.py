class dsu:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*(n)

    def findPar(self, x):
        if x != self.par[x]:
            self.par[x] = self.findPar(self.par[x])
        return self.par[x]

    def union(self, n1, n2):
        p1, p2 = self.findPar(n1), self.findPar(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class solution:
    def largestIsland(self, grid: list[list[int]]) -> int:

        n = len(grid)

        def isValid(r, c):
            if r < 0 or c < 0 or r >= n or c >= n:
                return False
            return True

        uf = dsu(n * n)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                for dr, dc in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
                    if isValid(r + dr, c + dc) and grid[r + dr][c + dc]:
                        nodeNo = r * n + c
                        adjNode = (r + dr) * n + (c + dc)
                        uf.union(nodeNo, adjNode)

        mx = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    continue
                visitComponent = set()
                for dr, dc in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
                    newR, newC = r + dr, c + dc
                    if isValid(newR, newC):
                        if grid[newR][newC]:
                            visitComponent.add(uf.findPar(newR * n + newC))
                sizeTot = 0
                for i in visitComponent:
                    sizeTot += uf.rank[i]
                mx = max(mx, sizeTot + 1)

        for cellNo in range(n * n):
            mx = max(mx, uf.rank[uf.findPar(cellNo)])

        return mx


x = solution()
print(x.largestIsland([[1, 0], [0, 1]]))
