class solution:
    def findRedundantConnection(self, edges: list[list[int]]):
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def findPar(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(x, y):
            if par[x] == par[y]:
                return False
            if par[x] > par[y]:
                par[x] = par[y]
                rank[x] += rank[y]
            else:
                par[y] = par[x]
                rank[y] += rank[x]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


x = solution()
print(x.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
