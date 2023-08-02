import collections


class solution:
    def bfsTraversal(self, graph: list[list[int]]):
        q = collections.deque([0])
        visited = set([0])
        res = []

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node)

                for n in graph[node]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
        return res


x = solution()
print(x.bfsTraversal([[1, 2], [0, 2, 3], [0, 1], [1]]))
