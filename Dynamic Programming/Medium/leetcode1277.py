class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        for r in range(rows - 1, - 1, -1):
            for c in range(cols - 1, -1, - 1):
                if matrix[r][c] == 0:
                    continue
                down = matrix[r + 1][c] if r + 1 < rows else 0
                right = matrix[r][c + 1] if c + 1 < cols else 0
                diag = matrix[r + 1][c + 1] if r + \
                    1 < rows and c + 1 < cols else 0

                matrix[r][c] = 1 + min(down, right, diag)
                res += matrix[r][c]
        return res


x = Solution()
print(x.countSquares(matrix=[
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))
