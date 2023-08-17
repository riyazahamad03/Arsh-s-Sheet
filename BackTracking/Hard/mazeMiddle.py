class solution:
    def isMidPossible(self, grid: list[list[int]]):
        n = len(grid)
        visit = set()
        path = []

        def dfs(r, c):
            if min(r, c) < 0 or max(r, c) >= n or (r, c) in visit:
                return False
            if r == n // 2 and c == n // 2:
                path.append([r, c])
                return True

            visit.add((r, c))
            path.append([r, c])

            if (dfs(r + grid[r][c], c) or
                dfs(r - grid[r][c], c) or
                dfs(r, c + grid[r][c]) or
                dfs(r, c - grid[r][c])):
                return True

            path.pop()  # Backtrack by removing the current position
            return False

        if dfs(0, 0):
            return path
        else:
            return None


x = solution()
result = x.isMidPossible([[3, 5, 4, 4, 7, 3, 4, 6, 3],
                          [6, 7, 5, 6, 6, 2, 6, 6, 2],
                          [3, 3, 4, 3, 2, 5, 4, 7, 2],
                          [6, 5, 5, 1, 2, 3, 6, 5, 6],
                          [3, 3, 4, 3, 0, 1, 4, 3, 4],
                          [3, 5, 4, 3, 2, 2, 3, 3, 5],
                          [3, 5, 4, 3, 2, 6, 4, 4, 3],
                          [3, 5, 1, 3, 7, 5, 3, 6, 4],
                          [6, 2, 4, 3, 4, 5, 4, 5, 1]])

if result:
    for point in result:
        print(point)
else:
    print("No valid path found.")
