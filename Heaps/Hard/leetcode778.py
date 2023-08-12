import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visit.add((0, 0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == n-1 and c == n-1:
                return t

            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                if min(newR, newC) < 0 or max(newR, newC) >= n or (newR, newC) in visit:
                    continue
                visit.add((newR, newC))
                heapq.heappush(minHeap, [max(t, grid[newR][newC]), newR, newC])


x = Solution()
print(x.swimInWater(grid=[[0, 2], [1, 3]]))
