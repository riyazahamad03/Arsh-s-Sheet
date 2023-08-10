class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # red
        # l , r = 0 , 0
        # while r < len(nums):
        #     if nums[r] == 0:
        #         nums[l] , nums[r] = nums[r] , nums[l]
        #         l += 1
        #     r += 1

        # # white
        # r = l
        # while r < len(nums):
        #     if nums[r] == 1:
        #         nums[l] , nums[r] = nums[r] , nums[l]
        #         l += 1
        #     r += 1

        l, r = 0, len(nums) - 1
        i = 0

        def swap(lo, hi):
            tmp = nums[lo]
            nums[lo] = nums[hi]
            nums[hi] = tmp
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
        return nums


x = Solution()
print(x.sortColors([2, 0, 2, 1, 1, 0]))
