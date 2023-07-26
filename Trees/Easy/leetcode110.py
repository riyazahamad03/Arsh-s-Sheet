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
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return [True, 0]
            left, right = dfs(node.left), dfs(node.right)
            balancedNode = (left[0] and right[0]) and abs(
                left[1] - right[1]) <= 1
            return [balancedNode, 1 + max(left[1], right[1])]
        return dfs(root)[0]


x = solution()
print(x.isBalanced(root))
