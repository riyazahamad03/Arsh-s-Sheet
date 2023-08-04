import collections


class solution:
    def numOfMinutes(Self, n: int, headID: int, manager: list[int], informTime: int):
        adj = collections.defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)
        q = collections.deque([(headID, 0)])  # head and time
        res = float("-inf")
        while q:
            head, time = q.popleft()
            res = max(res, time)
            for child in adj[head]:
                q.append((child, time + informTime[head]))

        return res


x = solution()
print(x.numOfMinutes(n=6, headID=2, manager=[
      2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))
