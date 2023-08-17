class solution:
    def maxCharRep(self, s: str, k: int):
        cnt = {}
        maxF = 0
        res = 0
        l = 0
        for r in range(len(s)):
            cnt[s[r]] = 1 + cnt.get(s[r], 0)
            maxF = max(maxF, cnt[s[r]])

            if (r - l + 1) - maxF > k:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


x = solution()
print(x.maxCharRep(s="ABAB", k=2))
