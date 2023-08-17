import math


class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        sumStone = sum(stones)
        tar = math.ceil(sumStone/2)

        dp = {}

        def dfs(i, tot):
            if tot >= tar or i == len(stones):
                return abs(tot - (sumStone - tot))
            if (i, tot) in dp:
                return dp[(i, tot)]

            dp[(i, tot)] = min(dfs(i + 1, tot), dfs(i + 1, tot + stones[i]))
            return dp[(i, tot)]
        return dfs(0, 0)


x = Solution()
print(x.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
