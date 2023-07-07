class Solution:
    def printPossiblePairs(self, nums: list[int], r: int):
        data, res = [], []

        def dfs(idx, start):
            if idx >= len(nums):
                return
            if len(data) == r:
                res.append(data.copy())
                return

            for i in range(start, len(nums)):
                data.append(nums[i])
                # print(data)
                dfs(idx + 1, i + 1)
                data.pop()

        dfs(0, 0)
        return res


x = Solution()
print(x.printPossiblePairs([1, 2, 3, 4, 5], 4))
