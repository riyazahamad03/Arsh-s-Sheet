import heapq


class solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int):
        maxVal = float("-inf")
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]

                if xj - xi > k:
                    break
                maxVal = max(maxVal, yi + yj + abs(xi - xj))
        return maxVal

# TLE


x = solution()
print(x.findMaxValueOfEquation(
    points=[[1, 3], [2, 0], [5, 10], [6, -10]], k=1))


class solution2:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int):
        maxVal = float("-inf")
        maxHeap = []
        for x, y in points:
            while maxHeap and x - maxHeap[0][1] > k:
                heapq.heappop(maxHeap)
            if maxHeap:
                currVal = -(maxHeap[0][0] + x + y)
                maxVal = max(maxVal, currVal)
            heapq.heappush(maxHeap, ((x - y), x))
        return maxVal


x = solution2()
print(x.findMaxValueOfEquation(
    points=[[1, 3], [2, 0], [5, 10], [6, -10]], k=1))
