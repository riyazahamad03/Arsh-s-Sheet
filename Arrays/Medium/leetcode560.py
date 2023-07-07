class solution:
    def subarraySum(self, nums: list[int], k: int):
        res = 0
        curSum = 0
        hashMap = {0 : 1}
        for i in nums:
            curSum += i
            if curSum - k in hashMap:
                res += hashMap[curSum - k]
            hashMap[curSum] = 1 + hashMap.get(curSum , 0)
        return res
x = solution()
print(x.subarraySum( nums = [1,1,1], k = 2))