class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in self.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


class solution:
    def findWords(self, board: list[str], words: list[str]):
        root = TrieNode()
        for w in words:
            root.addWord(w)
        rows, cols = len(board), len(board[0])
        visit, res = set(), []

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or board[r][c] not in node.children:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.append(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return res


x = solution()
print(x.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
print(x.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], [
      "i", "h", "k", "r"], ["i", "f", "l", "v"]], words=["oath", "pea", "eat", "rain"]))
