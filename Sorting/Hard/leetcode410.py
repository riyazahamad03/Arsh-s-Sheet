class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        def canSplit(val):
            subArray = 0
            currSum = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    subArray += 1
                    currSum = n
            return subArray + 1 <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = l + ((r - l)//2)
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res


x = Solution()
print(x.splitArray(nums=[7, 2, 5, 10, 8], k=2))
