class Solution:
    def isNegativeWeightCycle(self, n, edges):
        dist = [float("inf") for _ in range(n)]
        dist[0] = 0

        for i in range(n - 1):
            for s, d, p in edges:
                if dist[s] == float("inf"):
                    continue
                if dist[s] + p < dist[d]:
                    dist[d] = dist[s] + p

        for s, d, p in edges:
            if dist[s] == float("inf"):
                continue
            if dist[s] + p < dist[d]:
                return 1

        return 0


x = Solution()
print(x.isNegativeWeightCycle(3, [[0, 1, -1], [1, 2, -2], [2, 0, -3]]))
