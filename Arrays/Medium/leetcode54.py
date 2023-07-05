class solution:
    def spiralOrder(self, matrix: list[list[int]]):
        res = []
        left, right = 0, len(matrix)
        top, bot = 0, len(matrix)

        while left < right and top < bot:
            for idx in range(left, right):
                res.append(matrix[top][idx])
            top += 1

            for jdx in range(top, bot):
                res.append(matrix[jdx][right - 1])
            right -= 1

            if not (top < bot and left < right):
                break

            for cdx in range(right-1, left - 1, -1):
                res.append(matrix[bot-1][cdx])
            bot -= 1

            for ddx in range(bot-1, top-1, -1):
                res.append(matrix[ddx][left])
            left += 1
        return res


x = solution()
print(x.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
