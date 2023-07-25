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


class solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode):
        if not t1 and not t2:
            return None

        v1, v2 = t1.val if t1 else 0, t2.val if t2 else 0

        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(
            t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTrees(
            t1.right if t2 else None, t2.right if t2 else None)

        return root


x = solution()
print(x.mergeTrees(root, root1))
