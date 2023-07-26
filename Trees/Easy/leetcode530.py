class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


class solution:
    def getMinimumDifference(self, root: TreeNode):
        prev, res = None, float("inf")

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal res, prev
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)
        dfs(root)
        return res


x = solution()
print(x.getMinimumDifference(root))
