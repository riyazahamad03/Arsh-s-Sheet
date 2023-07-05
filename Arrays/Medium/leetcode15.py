class solution:
    def threeSum(self, nums: list[int]):
        res = []
        nums.sort()
        for i, e in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                targetSum = e + nums[l] + nums[r]
                if targetSum > 0:
                    r -= 1
                elif targetSum < 0:
                    l += 1
                else:
                    res.append([e, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


x = solution()
print(x.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
