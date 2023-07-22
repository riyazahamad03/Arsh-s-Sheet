import collections


class solution:
    def nearest(self, grid: list[list[int]]):
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()

        # collecting the initial ones and passing their value to 0 because initial ones require zero step
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    visit.add((r, c))
                    q.append((r, c))
                    grid[r][c] = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        Length = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = dr + r, dc + c
                    if newR < 0 or newR >= rows or newC < 0 or newC >= cols or (newR, newC) in visit:
                        continue
                    visit.add((newR, newC))
                    q.append((newR, newC))
                    grid[newR][newC] = Length
            Length += 1
        return grid


x = solution()
print(x.nearest([[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]))
