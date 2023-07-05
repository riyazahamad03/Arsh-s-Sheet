class solution:
    def maxScore(self, cardPoints: list[int], k: int):
        l, r = 0, len(cardPoints) - k
        tot = sum(cardPoints[r:])
        res = tot
        while r < len(cardPoints):
            tot += cardPoints[l] - cardPoints[r]
            res = max(res, tot)
            l += 1
            r += 1
        return res


x = solution()
print(x.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
