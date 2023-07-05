class solution:
    def findDuplicate(self, nums: list[int]):
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(abs(idx) + 1)
            nums[idx] = - nums[idx]
        return res


x = solution()
print(x.findDuplicate([1, 1, 2, 3, 4, 4, 5]))
