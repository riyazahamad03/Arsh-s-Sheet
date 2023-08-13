class solution:
    def climbingStairs(self, n: int):
        dp = {}

        def dfs(i):

            if i > n:
                return 0
            if i == n:
                return 1
            if i in dp:
                return dp[i]

            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]
        return dfs(0)

    def climbingStairs2(self, n: int):
        one, two = 1, 1
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one


x = solution()
print(x.climbingStairs(2))
print(x.climbingStairs2(2))
