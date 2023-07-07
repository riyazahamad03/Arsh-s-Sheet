class solution:
    def subArrayDivByK(self, nums: list[int], k: int):
        res = 0
        for idx in range(len(nums)):
            S = 0
            for jdx in range(idx, len(nums)):
                S += nums[jdx]
                if S % k == 0:
                    res += 1
        return res


# TLE SOLUTION
# TIME COMPLEXITY O(N^2)
x = solution()
print(x.subArrayDivByK([4, 5, 0, -2, -3, 1], 5))


class solution2:
    def subArrayDivByK(self, nums: list[int], k: int):
        prefixSum = 0
        count = {}
        count[0] = 1
        res = 0
        for idx in range(len(nums)):
            prefixSum = (prefixSum + nums[idx]) % k
            if prefixSum in count:
                res += count[prefixSum]
            count[prefixSum] = 1 + count.get(prefixSum, 0)
        return res


x = solution2()
print(x.subArrayDivByK([4, 5, 0, -2, -3, 1], 5))
