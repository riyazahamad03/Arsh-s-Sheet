class solution:
    def trap(self, heights: list[int]):
        if not heights:
            return 0
        l, r = 0, len(heights) - 1
        lMax, rMax = heights[l], heights[r]
        res = 0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, heights[l])
                res += lMax - heights[l]
            else:
                r -= 1
                rMax = max(rMax, heights[r])
                res += rMax - heights[r]
        return res


x = solution()
print(x.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
