import collections


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        time, freshOranges = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        Queue = collections.deque()

        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 1:
                    freshOranges += 1

                if grid[i][j] == 2:
                    Queue.append([i, j])

        # BFS algo comes into Play
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while Queue and freshOranges > 0:
            for i in range(len(Queue)):
                row, col = Queue.popleft()
                for dr, dc in directions:
                    if (dr + row < 0 or
                                dc + col < 0 or
                                dr + row >= ROWS or
                                dc + col >= COLS or
                                grid[dr + row][dc + col] != 1
                            ):

                        continue
                    grid[dr + row][dc + col] = 2
                    freshOranges -= 1
                    Queue.append([dr + row, dc + col])
            time += 1
        return time if freshOranges == 0 else -1


x = Solution()
print(x.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
