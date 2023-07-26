import collections


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
    def sumOfLeftLeaves(self, root: TreeNode):
        lSum = 0
        q = collections.deque([(root, 'r')])
        while q:
            for _ in range(len(q)):
                node, pos = q.popleft()
                if pos == 'l' and not node.left and not node.right:
                    lSum += node.val
                if node.left:
                    q.append((node.left, 'l'))
                if node.right:
                    q.append((node.right, 'r'))
        return lSum


x = solution()
print(x.sumOfLeftLeaves(root))
