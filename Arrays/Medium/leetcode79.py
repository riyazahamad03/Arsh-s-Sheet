class Solution:
    def exist(self, board: list[list[str]], word: str):
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(row, col, idx):
            if idx >= len(word):
                return True
            if (row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visit or board[row][col] != word[idx]):
                return False
            visit.add((row, col))

            res = (dfs(row + 1, col, idx + 1) or
                   dfs(row, col + 1, idx + 1) or
                   dfs(row - 1, col, idx + 1) or
                   dfs(row, col - 1, idx + 1))
            visit.remove((row, col))
            return res
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False


x = Solution()
print(x.exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))

print(x.exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))

print(x.exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
