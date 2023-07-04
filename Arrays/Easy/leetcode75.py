class solution:
    def sortColor(self, nums: list[int]):
        l, r = 0, 0
        while r < len(nums):
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        r = l
        while r < len(nums):
            if nums[r] == 1:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        return nums


class solution2:
    def sortColor(self, nums: list[int]):
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i < r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
        return nums


x = solution()
print(x.sortColor(nums=[2, 0, 2, 1, 1, 0]))
print(x.sortColor(nums=[2, 0, 1]))

x = solution2()
print(x.sortColor(nums=[2, 0, 2, 1, 1, 0]))
