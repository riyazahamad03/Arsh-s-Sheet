class solution:
    def largestRectangleArea(self, heights: list[int]):
        maxArea, stack = 0, []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][-1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


x = solution()
print(x.largestRectangleArea([2, 1, 5, 6, 2, 3]))
