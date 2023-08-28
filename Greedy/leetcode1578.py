class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res, curr = 0, 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                curr = 0
            res += min(curr, neededTime[i])
            curr = max(curr, neededTime[i])
        return res


x = Solution()
print(x.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
