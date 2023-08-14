class solution:
    def combinationSum2(self, candidates: list[int], target: int):
        candidates.sort()
        res = []

        def backtrack(idx, tot, curr):
            if target == tot:
                res.append(curr.copy())
                return
            if tot > target or idx >= len(candidates):
                return

            curr.append(candidates[idx])
            backtrack(idx + 1, tot + candidates[idx], curr)
            curr.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1

            backtrack(idx + 1, tot, curr)
        backtrack(0, 0, [])
        return res
x = solution()
print(x.combinationSum2([10,1,2,7,6,1,5] , 8))
