class solution:
    def maximumProduct(self, nums: list[int]):
        nums.sort()
        return max(nums[0] * nums[1] * nums[- 1], nums[-1] * nums[-2] * nums[-3])

    def maximumProduct2(self, nums: list[int]):
        min1 = min2 = float("inf")
        max1 = max2 = max3 = float("-inf")

        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n

            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n
        return max(min1 * min2 * max1, max1*max2*max3)


x = solution()
print(x.maximumProduct([1, 2, 3]))
print(x.maximumProduct2([1, 2, 3]))
