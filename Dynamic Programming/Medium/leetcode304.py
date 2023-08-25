class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.mat = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            pref = 0
            for c in range(cols):
                pref += matrix[r][c]
                above = self.mat[r][c + 1]
                self.mat[r + 1][c + 1] = pref + above

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
        btmRight = self.mat[r2][c2]
        above = self.mat[r1 - 1][c2]
        left = self.mat[r2][c1 - 1]
        topLeft = self.mat[r1 - 1][c1 - 1]

        return btmRight - above - left + topLeft


x = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(NumMatrix.sumRegion([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1],
                           [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]], 2, 1, 4, 3))
