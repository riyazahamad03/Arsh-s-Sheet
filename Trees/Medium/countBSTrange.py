class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(11)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(6)
root.left.right.left.right = TreeNode(4)


class solution:
    def getCount(self, root, low, high):
        res = 0

        def dfs(node):
            if not node:
                return
            nonlocal res
            if low <= node.val and node.val <= high:
                res += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res


x = solution()
print(x.getCount(root, 2, 11))
