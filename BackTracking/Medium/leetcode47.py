import collections


class solution:
    def permuteUnique(self, nums: list[int]):
        res, perms = [], []
        count = collections.Counter(nums)

        def backTrack():
            if len(nums) == len(perms):
                res.append(perms.copy())
                return
            for n in count:
                if count[n] > 0:

                    perms.append(n)
                    count[n] -= 1

                    backTrack()

                    count[n] += 1
                    perms.pop()
        backTrack()
        return res


x = solution()
print(x.permuteUnique([1, 1, 2]))
