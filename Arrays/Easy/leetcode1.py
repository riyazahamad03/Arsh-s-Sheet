class solution:
    def twoSum(self, nums: list[int], target: int):
        d = {}
        for idx in range(len(nums)):
            if (target - nums[idx]) in d:
                return [d[target - nums[idx]], idx]
            d[nums[idx]] = idx


x = solution()
print(x.twoSum(nums=[2, 7, 11, 15], target=9))
