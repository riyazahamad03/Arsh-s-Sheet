import collections


class solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]):
        adj = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def bfs(src, dest):
            if src not in adj or dest not in adj:
                return -1
            q, visit = collections.deque(), set()
            q.append([src, 1])
            while q:
                node, w = q.popleft()
                if node == dest:
                    return w
                for nei, weight in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append([nei, w * weight])
            return -1
        return [bfs(src, dest) for src, dest in queries]


x = solution()
print(x.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[
      2.0, 3.0], queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
