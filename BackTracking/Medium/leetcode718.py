class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        d = [[0 for _ in range(len(nums1)+1)] for _ in range(len(nums2)+1)]
        res = 0
        for r in range(len(nums2) - 1, -1, -1):
            for c in range(len(nums1) - 1, -1, -1):
                if nums1[c] == nums2[r]:
                    d[r][c] = 1 + d[r + 1][c + 1]
                    res = max(res, d[r][c])
        return res


x = Solution()
print(x.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))
