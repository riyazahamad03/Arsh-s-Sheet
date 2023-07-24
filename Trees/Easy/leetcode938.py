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
    def rangeSumBst(self, root: TreeNode, low: int, high: int):
        Sum = 0

        def dfs(node):
            nonlocal Sum

            if not node:
                return 0
            if node.val >= low and node.val <= high:
                Sum += node.val

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return Sum


x = solution()
print(x.rangeSumBst(root, 1,  5))
