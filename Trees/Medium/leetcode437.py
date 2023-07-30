class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)


class solution:
    def __init__(self):
        self.cnt = 0
        self.freq = {0: 1}

    def pathSum(self, root: TreeNode, targetSum=0):
        def dfs(node, ps):
            if not node:
                return
            cs = ps + node.val
            x = cs - targetSum

            if x in self.freq:
                self.cnt += self.freq[x]

            if cs in self.freq:
                self.freq[cs] += 1
            else:
                self.freq[cs] = 1

            dfs(node.left, cs)
            dfs(node.right, cs)
            self.freq[cs] -= 1
        dfs(root, 0)
        return self.cnt


x = solution()
print(x.pathSum(root, 8))
