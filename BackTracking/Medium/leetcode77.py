class solution:
    def combine(self, n: int, k: int):
        res = []

        def backTrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)
                backTrack(i + 1 , comb)
                comb.pop()
        backTrack(1, [])
        return res


x = solution()
print(x.combine(4, 2))
