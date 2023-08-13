class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])

            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] = -1 * (nums[val - 1])
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1


x = Solution()
print(x.firstMissingPositive(nums=[1, 2, 0]))
print(x.firstMissingPositive(nums=[3, 4, -1, 1]))
