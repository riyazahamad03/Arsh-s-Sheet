class dsu:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*(n)

    def findPar(self, x):
        if x != self.par[x]:
            self.par[x] = self.findPar(self.par[x])
        return self.par[x]

    def union(self, n1, n2):
        p1, p2 = self.findPar(n1), self.findPar(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        DSU = dsu(20005)
        for st in stones:
            DSU.union(st[0], st[1] + 10001)
        compSet = set()
        for st in stones:
            compSet.add(DSU.findPar(st[0]))
        comps = len(compSet)
        return len(stones) - comps


x = Solution()
print(x.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
