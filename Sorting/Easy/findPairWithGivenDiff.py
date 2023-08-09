class solution:
    def findDifference(self, nums: list[int], target: int):
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[r] - nums[l] == target:
                return (nums[l], nums[r])

            if nums[r] - nums[l] > target:
                l += 1
            else:
                r -= 1
        return -1


x = solution()
print(x.findDifference([5, 20, 3, 2, 50, 80], 12))
