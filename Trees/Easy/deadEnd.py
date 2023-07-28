import collections


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
    def isDeadEnd(self, root: TreeNode):
        def dfs(node, left, right):
            if not node:
                return False
            if left >= right:
                return True
            l, r = dfs(node.left, left, node.val -
                       1), dfs(node.right, node.val + 1, right)
            return l or r
        return dfs(root, 1, float("inf"))


x = solution()
print(x.isDeadEnd(root))
