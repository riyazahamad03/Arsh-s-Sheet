class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        newNode = TreeNode(data)
        if not self.root:
            self.root = newNode
        else:
            curr = self.root
            while True:
                if data < curr.val:
                    if curr.left == None:
                        curr.left = newNode
                        break
                    else:
                        curr = curr.left
                elif data > curr.val:
                    if curr.right == None:
                        curr.right = newNode
                        break
                    else:
                        curr = curr.right


class solution:
    def diameterOfBinaryTree(self, root: TreeNode):
        res = float("-inf")

        def dfs(node):
            nonlocal res
            if not node:
                return -1
            l = dfs(node.left)
            r = dfs(node.right)

            res = max(res, l + r + 2)
            return 1 + max(l, r)

        dfs(root)
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

x = solution()
print(x.diameterOfBinaryTree(root))
