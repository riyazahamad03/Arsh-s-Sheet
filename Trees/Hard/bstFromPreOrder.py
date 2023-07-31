class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class solution:
    def __init__(self):
        self.idx = 0

    def bstFromPreOrder(self, preOrder: list[int]):

        def dfs(low, high):

            if low > high:
                return None

            node = TreeNode(preOrder[self.idx])
            self.idx += 1

            if low == high:
                return node
            right = -1

            for i in range(low, high + 1):
                if preOrder[i] > node.val:
                    right = i
                    break
            if right == -1:
                right = self.idx + (high - low)

            node.left = dfs(self.idx, right - 1)
            node.right = dfs(right, high)
            return node
        return dfs(0, len(preOrder) - 1)


x = solution()
print(x.bstFromPreOrder([10, 5, 1, 7, 40, 50]))
