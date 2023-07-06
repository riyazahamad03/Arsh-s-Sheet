class solution:
    def gameOfLife(self, board: list[list[int]]):
        rows, cols = len(board), len(board[0])

        def totNei(r, c):
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == rows or j == cols):
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei

        for i in range(rows):
            for j in range(cols):
                nei = totNei(i, j)
                if board[i][j] == 1:
                    if nei in [2, 3]:
                        board[i][j] = 3
                elif nei == 3:
                    board[i][j] = 2
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                    board[i][j] = 1
        return board


x = solution()
print(x.gameOfLife(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
