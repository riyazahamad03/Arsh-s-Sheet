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
    def hasPathSum(self, root: TreeNode, target: int):
        def dfs(node, pathSum):
            if not node:
                return pathSum
            pathSum += node.val
            if not node.left and not node.right:
                return pathSum == target
            return (dfs(node.left, pathSum) or dfs(node.right, pathSum))
        return dfs(root, 0)


x = solution()
print(x.hasPathSum(root, 4))
