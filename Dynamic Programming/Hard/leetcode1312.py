class Solution:
    def minInsertions(self, s: str) -> int:
        res, dp = 0, {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            if s[l] != s[r]:
                dp[(l, r)] = 1 + min(dfs(l + 1, r), dfs(l, r - 1))
            else:
                dp[(l, r)] = dfs(l + 1, r - 1)
            return dp[(l, r)]
        return dfs(0, len(s) - 1)


x = Solution()
print(x.minInsertions(s="mbadm"))
