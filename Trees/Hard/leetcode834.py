import collections


class solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        res = [0] * (n)
        count = [1] * (n)
        self.root = 0
        def dfs(curr, par, depth):
            out = 1
            for ch in graph[curr]:
                if ch != par:
                    out += dfs(ch, curr, depth + 1)
                    self.root += (depth + 1)
            count[curr] = out
            return out
        dfs(0, - 1, 0)
        # print(count , self.root)


        def dfs2(curr, par, ans ):
            res[curr] = ans
            for ch in graph[curr]:
                if ch != par:
                    dfs2(ch, curr, ans + (n - count[ch]) - count[ch])
        dfs2(0, -1, self.root)
        return res


x = solution()
print(x.sumOfDistancesInTree(n=6, edges=[
      [0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
