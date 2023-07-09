class solution:
    def printDuplicate(self, s: str):
        res = []
        d = {}
        for i in s:
            d[i] = 1 + d.get(i, 0)

        for i in d:
            if d[i] > 1:
                res.append(i)
        return res


x = solution()
print(x.printDuplicate('GeeksForGeeks'))
