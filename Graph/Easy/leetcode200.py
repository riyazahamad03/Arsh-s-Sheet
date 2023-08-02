class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or (row, col) in visited
                or grid[row][col] == "0"
            ):
                return False
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            return True

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    if dfs(r, c):
                        ans += 1
        return ans


x = Solution()
print(
    x.numIslands(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
