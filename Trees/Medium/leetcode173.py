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


class binaryIterator:
    def __init__(self, root):
        self.stack = []

        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self):
        res, curr = None, None
        if self.stack:
            res = self.stack.pop()
        if res:
            curr = res.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return res.val

    def hasNext(self):
        return len(self.stack) > 0


bst = binaryIterator(root)
print(bst.next())
print(bst.next())
print(bst.hasNext())
