class solution:
    def smallestWindow(self, S, P):
        if not P:
            return ""
        sCount, pCount = {}, {}
        for i in P:
            pCount[i] = 1 + pCount.get(i, 0)

        have, need = 0, len(P)
        res, resLen = [-1, - 1], float("inf")
        l = 0
        for r in range(len(S)):
            sCount[S[r]] = 1 + sCount.get(S[r], 0)
            if S[r] in pCount and sCount[S[r]] == pCount[S[r]]:
                have += 1
            while have == need:
                if (r - l - 1) < resLen:
                    resLen = r - l - 1
                    res = [l, r]
                sCount[S[l]] -= 1
                if S[l] in pCount and sCount[S[l]] < pCount[S[l]]:
                    have -= 1
                l += 1
        l, r = res
        return S[l: r + 1] if resLen != float("inf") else ""


x = solution()
print(x.smallestWindow("zoomlazapzo", "oza"))
