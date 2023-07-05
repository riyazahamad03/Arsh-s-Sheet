class solution:
    def fourSum(self, nums: list[int], target: int):
        quad, res = [], []
        nums.sort()
        print(nums)

        def kSum(k, start):
            if k > 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1)
                    quad.pop()
                return
            l, r = start, len(nums) - 1
            while l < r:
                fourSum = sum(quad) + nums[l] + nums[r]
                if fourSum > target:
                    r -= 1
                elif fourSum < target:
                    l += 1
                else:
                    res.append([quad + [nums[l], nums[r]]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        kSum(4, 0)
        return res


x = solution()
print(x.fourSum([1, 0, -1, 0, -2, 2], target=0))
