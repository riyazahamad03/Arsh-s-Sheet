class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quickSelct(l, r):
            piv, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= piv:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quickSelct(l, p - 1)
            elif p < k:
                return quickSelct(p + 1, r)
            else:
                return nums[p]
        return quickSelct(0, len(nums) - 1)


x = Solution()
print(x.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
