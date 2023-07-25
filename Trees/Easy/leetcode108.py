class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class solution:
    def sortedArrayBST(self, nums: list[int]):
        def createNode(left, right):
            if left > right:
                return
            mid = (left + right)//2
            root = TreeNode(nums[mid])

            root.left = createNode(left, mid - 1)
            root.right = createNode(mid + 1, right)

            return root
        return createNode(0, len(nums) - 1)


x = solution()
print(x.sortedArrayBST([1, 2, 3]))
