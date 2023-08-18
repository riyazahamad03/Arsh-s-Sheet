class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            tmp = currMax * n
            currMax = max(n, currMax * n, currMin * n)
            currMin = min(n, tmp, currMin * n)

            res = max(res, currMax)
        return res


x = Solution()
print(x.maxProduct(nums=[2, 3, -2, 4]))
