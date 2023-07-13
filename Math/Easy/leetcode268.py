class solution:
    def missingNumber(self, nums: list[int]):
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res


x = solution()
print(x.missingNumber([3, 0, 1]))
