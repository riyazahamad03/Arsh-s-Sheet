class solution:
    def removeDuplicate(self, nums: list[int]):
        l, r = 1, 1
        while r < len(nums):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return (l, nums)


x = solution()
print(x.removeDuplicate([1, 1, 2]))
