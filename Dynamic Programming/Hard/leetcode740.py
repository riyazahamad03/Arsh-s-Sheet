from collections import Counter
class solution:
    def deleteAndEarn(self , nums : list[int]):
        count = Counter(nums)
        nums = sorted(set(nums))

        earn1 , earn2 = 0 , 0
        for i in range(len(nums)):
            currEarn = nums[i] * (count[nums[i]])

            if i > 0 and nums[i] == nums[i - 1] + 1:
                tmp = earn2
                earn2 = max(earn2 , currEarn + earn1)
                earn1 = tmp
            else:
                tmp = earn2
                earn2 = earn2 + currEarn
                earn1 = tmp
        return earn2
x = solution()
print(x.deleteAndEarn(nums = [3,4,2]))