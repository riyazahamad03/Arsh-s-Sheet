class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)


class solution:
    def recoverTrees(self, root: TreeNode):
        curr = root
        prev = TreeNode(float("-inf"))
        replace = []
        stack = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if node.val < prev.val:
                replace.append([prev, node])
            prev = node
            curr = node.right
        replace[0][0].val, replace[-1][-1].val = replace[-1][-1].val, replace[0][0].val
        return root


x = solution()
res = x.recoverTrees(root)
