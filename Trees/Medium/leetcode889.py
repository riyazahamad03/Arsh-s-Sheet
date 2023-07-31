class TreeNode:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]):
        def dfs(preStart, preEnd, postStart, postEnd):
            if preStart > preEnd:
                return None

            node = TreeNode(preorder[preStart])
            if preStart == preEnd:
                return node
            idx = postStart
            while postorder[idx] != preorder[preStart + 1]:
                idx += 1
            totalElem = idx - postStart + 1

            node.left = dfs(preStart + 1, preStart + totalElem, postStart, idx)
            node.right = dfs(preStart + totalElem + 1,
                             preEnd, idx + 1, postEnd - 1)
            return node

        return dfs(0, len(preorder) - 1, 0, len(postorder) - 1)


x = Solution()
print(x.constructFromPrePost(
    preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1]))
