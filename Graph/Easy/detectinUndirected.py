class solution:
    def detectCycle(v : int , adj : list[list[int]]):
        visit = set()
        
        def dfs(node , par):
            visit.add(node)

            for nei in adj[node]:
                if nei not in visit:
                    if dfs(nei , node):
                        return True
                    elif nei != par:
                        return True
            return False
        for i in range(v):
            if i not in visit:
                if dfs(i , -1):
                    return 1
        return 0