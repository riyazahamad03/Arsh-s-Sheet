class solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]):
        res = [-1] * len(nums1)
        numsIdx = {nums1[i]: i for i in range(len(nums1))}

        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = numsIdx[val]
                res[idx] = curr
            if curr in numsIdx:
                stack.append(curr)
        return res


x = solution()
print(x.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
