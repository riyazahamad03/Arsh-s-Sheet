class solution:
    def LENGTHOFLIS(self, nums: list[int]):
        longest = [1] * (len(nums))

        for i in range(len(nums) - 1,  - 1, - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    longest[i] = max(longest[i], 1 + longest[j])
        return max(longest)


x = solution()
print(x.LENGTHOFLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
