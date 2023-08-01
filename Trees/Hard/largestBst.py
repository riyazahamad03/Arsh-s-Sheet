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


class Solution:
    class Node:  # Move the 'Node' class inside 'Solution'
        def __init__(self, maxVal, minVal, maxSize):
            self.maxVal = maxVal
            self.minVal = minVal
            self.maxSize = maxSize

    def largestBst(self, root: TreeNode):
        def dfs(node):
            if not node:
                return self.Node(float("inf"), float("-inf"), 0)
            left = dfs(node.left)
            right = dfs(node.right)

            if left.maxVal < node.val < right.minVal:  # Simplify the condition
                return self.Node(
                    max(node.val, right.maxVal),
                    min(node.val, left.minVal),
                    left.maxSize + right.maxSize + 1,
                )
            else:
                return self.Node(
                    float("-inf"), float("inf"), max(left.maxSize, right.maxSize)
                )

        return dfs(root).maxSize


x = Solution()
print(x.largestBst(root))
