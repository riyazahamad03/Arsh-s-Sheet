class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, - 1):
                bot = int(matrix[r + 1][c]) if r + 1 < rows else 0
                right = int(matrix[r][c + 1]) if c + 1 < cols else 0
                diag = int(matrix[r + 1][c + 1]) if r + \
                    1 < rows and c + 1 < cols else 0

                if matrix[r][c] == "1":
                    matrix[r][c] = 1 + min(bot, right, diag)
                    res = max(res, matrix[r][c])
        return res ** 2


x = Solution()
print(x.maximalSquare(matrix=[["1", "0", "1", "0", "0"], [
      "1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
