class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val


class solution:
    def uniqueBinarySearchTree(self, n: int):
        def helper(left, right):
            if left > right:
                return [None]
            trees = []
            for root in range(left, right + 1):
                for l in helper(left, root - 1):
                    for r in helper(root + 1, right):
                        node = TreeNode(root)
                        node.left = l
                        node.right = r

                        trees.append(node)
            return trees
        return helper(1, n)
x = solution()
print(x.uniqueBinarySearchTree(3))
