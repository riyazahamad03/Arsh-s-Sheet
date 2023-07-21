class solution:
    def mctFromLeafNode(self, arr: list[int]):
        maxi = {}
        for i in range(len(arr)):
            maxi[(i, i)] = arr[i]
            for j in range(i + 1, len(arr)):
                maxi[(i, j)] = max(arr[j], maxi[(i, j - 1)])

        dp = {}

        def dfs(left, right):
            if right - left == 0:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            res = float("inf")
            for idx in range(left, right):
                res = min(
                    res,  maxi[(left, idx)] * maxi[(idx + 1, right)] + dfs(left, idx) + dfs(idx + 1, right))
            dp[(left, right)] = res
            return res
        return dfs(0, len(arr) - 1)


x = solution()
print(x.mctFromLeafNode([6, 2, 4]))

