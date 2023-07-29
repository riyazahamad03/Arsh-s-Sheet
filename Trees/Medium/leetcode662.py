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
    def widthOfBinaryTree(self, root: TreeNode):

        res = 0
        q = collections.deque([(root, 0)])
        while q:
            lMin, rMax = float("inf"), float("-inf")
            for _ in range(len(q)):
                node, length = q.popleft()
                lMin, rMax = min(lMin, length), max(rMax, length)
                if node.left:
                    q.append((node.left, length * 2))
                if node.right:
                    q.append((node.right, length * 2 + 1))
            res = max(res, (rMax - lMin) + 1)
        return res


x = solution()
print(x.widthOfBinaryTree(root))
