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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        curr = root
        while curr:
            value = curr.val
            if value > p.val and value > q.val:
                curr = curr.left
            elif value < p.val and value < q.val:
                curr = curr.right
            else:
                return curr.val


x = solution()
print(x.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)))
