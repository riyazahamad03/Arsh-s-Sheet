import collections


class Solution:
    def isBipartite(self, graph: list[list[int]]):
        odd = [0] * (len(graph))

        def bfs(i):
            if odd[i]:
                return True
            q = collections.deque([i])
            odd[i] = -1
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if odd[nei] == odd[node]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[node]
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True


x = Solution()
print(x.isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(x.isBipartite(graph=[[1, 3], [0, 2], [1, 3], [0, 2]]))
