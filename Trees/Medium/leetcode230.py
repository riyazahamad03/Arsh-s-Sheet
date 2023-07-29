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


class solution:
    def kthSmallest(self, root: TreeNode, k: int):
        stack = []
        curr = root
        n = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            n += 1
            if n == k:
                return node.val
            curr = curr.right


x = solution()
print(x.kthSmallest(root, 1))
