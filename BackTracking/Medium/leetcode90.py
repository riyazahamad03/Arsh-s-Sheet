class solution:
    def subsetWithDup(self, nums: list[int]):
        res, sub = [], []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res


x = solution()
print(x.subsetWithDup([1, 2, 2]))
