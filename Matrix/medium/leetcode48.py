class solution:
    def rotate(self, grid: list[list[int]]):
        l, r = 0, len(grid) - 1
        while l <= r:
            for i in range(l, r):
                top, bot = l, r
                # saving top left element
                tmp = grid[top][l + i]

                # bottom left to top left
                grid[top][l + i] = grid[bot - i][l]

                # bottom right to bottom left
                grid[bot - i][l] = grid[bot][r - i]

                # top right to bottom right
                grid[bot][r - i] = grid[top + i][r]

                # move top left to top right
                grid[top + i][r] = tmp
            l += 1
            r -= 1
        return grid


x = solution()
print(x.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
