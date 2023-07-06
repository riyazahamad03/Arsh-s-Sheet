class solution:
    def canJump(self, nums: list[int]):
        goalPost = len(nums) - 1
        for i in range(len(nums) - 1, - 1, - 1):
            if i + nums[i] >= goalPost:
                goalPost = i
        return True if not goalPost else False


x = solution()
print(x.canJump([2, 3, 1, 1, 4]))
