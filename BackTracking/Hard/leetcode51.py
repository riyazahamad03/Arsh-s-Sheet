class Solution:
    def solveNQueens(self, n: int):
        colCheck = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for row in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in colCheck or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                colCheck.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                board[r][c] = "Q"

                dfs(r + 1)

                board[r][c] = "."
                colCheck.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
        dfs(0)
        return res


x = Solution()
print(x.solveNQueens(4))
