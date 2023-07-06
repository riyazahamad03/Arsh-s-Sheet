class solution:
    def majorityElement(self, nums: list[int]):
        res, cnt = 0, 0
        for n in nums:
            if cnt == 0:
                res = n
            cnt += (1 if res == n else -1)
        return res


x = solution()
print(x.majorityElement(nums=[3, 2, 3]))
