class solution:
    def minMoves(self, nums: list[int]):
        nums.sort()
        S = 0
        for i in range(len(nums) - 1, 0, -1):
            S += nums[i] - nums[0]
        return S


x = solution()
print(x.minMoves([1, 2, 3]))
