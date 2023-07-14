class solution:
    def convertToTitle(self, columnNumber: int):
        res = ""
        while columnNumber:
            char = chr(ord('A') + (columnNumber - 1) % 26)
            res = char + res
            columnNumber = (columnNumber - 1)//26

        return res


x = solution()
print(x.convertToTitle(701))
