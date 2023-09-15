class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        r, l = 1, 0
        res = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                res += prices[r] - prices[l]
            l += 1
            r += 1
        return res


x = Solution()
print(x.maxProfit([7, 1, 5, 3, 2, 7]))
