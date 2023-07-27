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
        def dfs(node):
            if not node:
                return 
            
            if node.val == p.val or node.val == q.val:
                return node
            l , r  = dfs(node.left) , dfs(node.right)
            if l and r:
                return node.val
            if l:
                return l.val
            if r:
                return r.val
        return dfs(root)
x = solution()
print(x.lowestCommonAncestor(root , TreeNode(3) , TreeNode(5)))

