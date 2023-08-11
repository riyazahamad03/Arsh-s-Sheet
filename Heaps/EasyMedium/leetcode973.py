import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int):
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)

        res = []
        while k:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res


x = Solution()
print(x.kClosest(points=[[1, 3], [-2, 2]], k=1))
