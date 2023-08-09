class solution:
    def findCeil(self, lst: list[int], x: int):
        l, r = 0, len(lst) - 1
        if x > lst[r]:
            return - 1

        while l <= r:
            m = (l + r)//2
            if x > lst[m]:
                l = m + 1
            else:
                r = m - 1
        return lst[l]


x = solution()
print(x.findCeil([1, 2, 8, 10, 10, 12, 19], 4))
