class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(11)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(5)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(6)
# root.left.right.left.right = TreeNode(4)


class solution:
    def flatten(self, root: TreeNode):
        def dfs(node):
            if not node:
                return None
            leftTail = dfs(node.left)
            rightTail = dfs(node.right)

            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None
            res = rightTail or leftTail or node
            return res
        return dfs(root)


x = solution()
print(x.flatten(root))
