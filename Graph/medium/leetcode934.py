import collections


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        path = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inValidPath(r, c):
            return r >= n or r < 0 or c >= n or c < 0
        visit = set()

        def dfs(r, c):
            if inValidPath(r, c) or (r, c) in visit or grid[r][c] == 0:
                return
            visit.add((r, c))
            for dr, dc in path:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0, collections.deque(visit)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in path:
                        if inValidPath(r + dr, c + dc) or (r + dr, c + dc) in visit:
                            continue
                        if grid[r + dr][c + dc] == 1:
                            return res
                        q.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
                res += 1
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    dfs(row, col)
                    return bfs()


x = Solution()
print(x.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
      1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
