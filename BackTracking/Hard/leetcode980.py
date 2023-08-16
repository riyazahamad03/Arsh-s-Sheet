class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, zeroCnt):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or (r, c) in visit):
                return 0
            if grid[r][c] == 2:

                return 1 if len(visit) == zeroCnt + 1 else 0

            visit.add((r, c))
            # zeroCnt -= 1

            totPath = dfs(r + 1, c, zeroCnt) + dfs(r - 1, c, zeroCnt) + \
                dfs(r, c + 1, zeroCnt) + dfs(r, c - 1, zeroCnt)
            visit.remove((r, c))
            # zeroCnt += 1
            return totPath

        zeroCnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    zeroCnt += 1
                if grid[i][j] == 1:
                    r, c = i, j
        visit = set()
        return dfs(r, c, zeroCnt)


x = Solution()
print(x.uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
