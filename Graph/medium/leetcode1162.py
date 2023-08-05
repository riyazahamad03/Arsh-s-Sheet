import collections


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        N = len(grid)
        q = collections.deque()
        visit = set()
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    q.append([r, c, 0])
                    visit.add((r, c))
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        res = 0
        while q:
            for _ in range(len(q)):
                r, c, length = q.popleft()
                res = length
                for dr, dc in directions:
                    nR, nC = dr + r, dc + c
                    if min(nR, nC) >= 0 and max(nR, nC) < N and (nR, nC) not in visit and grid[nR][nC] == 0:
                        q.append((nR, nC, length + 1))
                        visit.add((nR, nC))
        return res if res >= 1 else -1


x = Solution()
print(x.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
