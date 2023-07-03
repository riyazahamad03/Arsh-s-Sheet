class solution:
    def findDuplicate(self, nums: list[int]):
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow1 = 0
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]

            if slow1 == slow:
                return slow1


x = solution()
print(x.findDuplicate(nums=[1, 3, 4, 2, 2]))
print(x.findDuplicate(nums=[3, 1, 3, 4, 2]))
