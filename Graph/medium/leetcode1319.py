class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def findPar(x):
            if x != par[x]:
                par[x] = findPar(par[x])
            return par[x]

        def union(n1, n2):
            p1, p2 = findPar(n1), findPar(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        if len(connections) >= n - 1:
            connected = n
            for n1, n2 in connections:
                if union(n1, n2):
                    connected -= 1

            return connected - 1
        else:
            return -1


x = Solution()
print(x.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
