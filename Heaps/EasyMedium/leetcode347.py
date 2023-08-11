class solution:
    def topKfrequent(self, nums: list[int], k: int):
        d = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for i in range(len(nums)):
            d[nums[i]] = 1 + d.get(nums[i], 0)

        for idx, val in d.items():
            freq[val].append(idx)

        for i in range(len(freq) - 1,  -1, -1):
            for t in freq[i]:
                res.append(t)
                k -= 1

                if k == 0:
                    return res


x = solution()
print(x.topKfrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
