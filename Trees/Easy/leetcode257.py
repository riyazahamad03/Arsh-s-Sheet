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
    def binaryTreePaths(self, root: TreeNode):
        res = []

        def dfs(node, s):
            if node:
                s += str(node.val)
            if not node.left and not node.right:
                res.append(s)
                return

            if node.left:
                dfs(node.left, s + "->")
            if node.right:
                dfs(node.right, s + "->")

        dfs(root, "")
        return res


x = solution()
print(x.binaryTreePaths(root))
