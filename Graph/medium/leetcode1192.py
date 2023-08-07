from collections import defaultdict


class Solution:
    def __init__(self):
        self.timer = 0

    def criticalConnections(self, n: int, connections: list[list[int]]):
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        tin = [-1] * n
        low = [-1] * n
        bridges = []

        def dfs(node, par):
            visit.add(node)
            tin[node] = self.timer
            low[node] = self.timer
            self.timer += 1

            for n in adj[node]:
                if n == par:
                    continue
                if n not in visit:
                    dfs(n, node)
                    low[node] = min(low[node], low[n])

                    if low[n] > tin[node]:
                        bridges.append([node, n])
                else:
                    low[node] = min(low[node], tin[n])

        dfs(0, -1)
        return bridges


x = Solution()
print(x.criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
