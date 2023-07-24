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

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)


class solution:
    def isSame(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)

        return False

    def isSubTree(self, root: TreeNode, subRoot:  TreeNode):
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSame(root, subRoot):
            return True

        return self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot)


x = solution()
print(x.isSubTree(root, root1))
