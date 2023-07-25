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
    def maxDepthUsingBfs(self, root: TreeNode):
        if not root:
            return 0
        q = collections.deque([root])
        maxDepth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
            maxDepth += 1
        return maxDepth

    def maxDepthUsingDfs(self, root: TreeNode):
        if not root:
            return 0
        maxDepth = 0

        def dfs(root, d):
            if not root:
                nonlocal maxDepth
                maxDepth = max(maxDepth, d)
                return
            dfs(root.left, d + 1)
            dfs(root.right, d + 1)
        dfs(root, 0)
        return maxDepth


x = solution()
print("Using BFS ", x.maxDepthUsingBfs(root))
print("Using DFS ", x.maxDepthUsingDfs(root))
