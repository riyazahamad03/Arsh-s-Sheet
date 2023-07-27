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
    def validateBST(self, root):
        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val and right > node.val):
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        return dfs(root, float("-inf"), float("inf"))


x = solution()
print(x.validateBST(root))
