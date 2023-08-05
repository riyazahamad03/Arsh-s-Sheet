import collections


class solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = collections.defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle = set()

        def dfs(idx):
            if idx in cycle:
                return False
            if not preMap[idx]:
                return True

            for node in preMap[idx]:
                if not dfs(node):
                    return False
            preMap[idx] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
    
x = solution()
print(x.canFinish(numCourses = 2, prerequisites = [[1,0]]))