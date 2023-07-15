class solution:
    def maxPoints(self, points: list[list[int]]):
        res = 1
        for i in range(len(points)):
            p1 = points[i]
            count = {}
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1] - p1[1])/(p2[0] - p1[0])
                count[slope] = 1 + count.get(slope, 1)

                res = max(res, count[slope])
        return res


x = solution()
print(x.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
