class solution:
    def ratMaze(self, board: list[list[int]]):
        rows, cols = len(board), len(board[0])
        res = []
        visit = set()

        def dfs(r, c, path):
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or board[r][c] == 0
                or (r, c) in visit
            ):
                return
            if r == rows - 1 and c == cols - 1:
                res.append(path)
                return
            visit.add((r, c))
            dfs(r + 1, c, path + "D")
            dfs(r - 1, c, path + "U")
            dfs(r, c + 1, path + "R")
            dfs(r, c - 1, path + "L")
            visit.remove((r, c))

        dfs(0, 0, "")
        return " ".join(res)


x = solution()
output = x.ratMaze([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]])
print(output)
