class Solution:
    def mergeSort(self, nums, low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        inv = self.mergeSort(nums, low, mid)
        inv += self.mergeSort(nums, mid + 1, high)
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if nums[i] > 2 * nums[j]:
                inv += mid - i + 1
                j += 1
            else:
                i += 1
        lst = []
        l, h = low, mid + 1
        while l <= mid and h <= high:
            if nums[l] <= nums[h]:
                lst.append(nums[l])
                l += 1
            else:
                lst.append(nums[h])
                h += 1
        while l <= mid:
            lst.append(nums[l])
            l += 1
        while h <= high:
            lst.append(nums[h])
            h += 1

        nums[low: high + 1] = lst[::]
        return inv

    def reversePairs(self, nums):
        return self.mergeSort(nums, 0, len(nums) - 1)


x = Solution()
print(x.reversePairs(nums=[1, 3, 2, 3, 1]))
