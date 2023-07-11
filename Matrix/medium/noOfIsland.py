class solution:
    def numIsland(self, grid: list[list[int]]):
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [[-1, 0], [0, - 1], [1, 0], [0, 1],
                      [1, 1], [- 1, -1], [1, - 1], [-1, 1]]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visit or not grid[i][j]:
                return
            visit.add((i, j))
            for dr, dc in directions:
                dfs(dr + i, dc + j)
        isLand = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c]:
                    dfs(r, c)
                    isLand += 1
        return isLand


x = solution()
print(x.numIsland([[0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0]]))
