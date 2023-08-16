class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [0] * (n + 1)
        res = 0

        def dfs(val):
            if val > n:
                nonlocal res
                res += 1
                return
            for i in range(1, n + 1):
                if nums[i] == 0 and (val % i == 0 or i % val == 0):
                    nums[i] = val

                    dfs(val + 1)

                    nums[i] = 0
        dfs(1)
        return res


x = Solution()
print(x.countArrangement(2))
