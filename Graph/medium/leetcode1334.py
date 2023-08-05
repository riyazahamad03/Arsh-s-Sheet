class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        dist = [[float("inf")] * (n) for _ in range(n)]

        for v1, v2, wt in edges:
            dist[v1][v2] = wt
            dist[v2][v1] = wt

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        cityCnt = n
        cityNo = -1

        for city in range(n):
            cnt = 0
            for adjCity in range(n):
                if dist[city][adjCity] <= distanceThreshold:
                    cnt += 1
            if cnt <= cityCnt:
                cityCnt = cnt
                cityNo = city
        return cityNo
    
x = Solution()
print(x.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
