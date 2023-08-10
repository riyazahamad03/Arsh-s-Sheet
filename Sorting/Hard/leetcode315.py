from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        sortedList = SortedList([])
        res = []
        for i in range(len(nums) - 1, - 1, - 1):
            idx = sortedList.bisect_left(nums[i])
            res.append(idx)
            sortedList.add(nums[i])
        return res[::-1]


x = Solution()
print(x.countSmaller([5, 2, 6, 1]))
