class solution:
    def moveZeros(self, nums: list[int]):
        l, r = 0, 0

        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


x = solution()
print(x.moveZeros(nums=[0, 1, 0, 3, 12]))
