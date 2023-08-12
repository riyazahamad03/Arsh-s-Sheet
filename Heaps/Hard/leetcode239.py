import collections


class solution:
    def slidingWindowMax(self, nums: list[int], k: int):
        res = []
        l, r = 0, 0
        q = collections.deque()
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1
        return res


x = solution()  
print(x.slidingWindowMax(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
