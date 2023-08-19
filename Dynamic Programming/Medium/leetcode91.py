class solution:
    def numDecodings(self  , s: str):
        dp = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in dp:
                return dp
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "0" and(s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)
x = solution()
print(x.numDecodings("12"))