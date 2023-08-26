class NumArray:

    def __init__(self, nums: list[int]):
        self.pre = []
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            self.pre.append(tot)
        

    def sumRange(self, left: int, right: int) -> int:
        right = self.pre[right]
        left = self.pre[left - 1] if left > 0 else 0
        return right - left
        
x = NumArray([-2, 0, 3, -5, 2, -1])
print(x.sumRange(0 , 2))