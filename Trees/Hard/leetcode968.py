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


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0
        camera = 0
        covered = set()
        covered.add(None)

        def dfs(node, parent):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

            if (not parent and node not in covered) or (
                node and node.left not in covered or node and node.right not in covered
            ):
                nonlocal camera
                camera += 1
                covered.add(node)
                covered.add(parent)
                covered.add(node.right)
                covered.add(node.left)

        dfs(root, None)
        return camera


x = Solution()
print(x.minCameraCover(root))
