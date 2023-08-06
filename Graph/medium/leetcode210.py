import collections


class solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]):
        cycle, visit = set(), set()
        res = []
        preReq = collections.defaultdict(list)

        for idx in prerequisites:
            preReq[idx[0]].append(idx[1])

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)

            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            visit.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res


x = solution()
print(x.findOrder(numCourses=2, prerequisites=[[1, 0]]))
