import collections


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
    def rightSidedView(self, root: TreeNode):
        res = []
        q = collections.deque([root])
        while q:
            right = None
            for _ in range(len(q)):
                node = q.popleft()

                right = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if right:
                res.append(right.val)
        return res


x = solution()
print(x.rightSidedView(root))
