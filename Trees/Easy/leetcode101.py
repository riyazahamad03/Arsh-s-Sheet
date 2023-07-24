class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


class solution:
    def isSymmetry(self, root: TreeNode):
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)


x = solution()
print(x.isSymmetry(root))
