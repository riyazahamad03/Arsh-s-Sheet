class solution:
    def intToRoman(self, num: int):
        sym = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000],
        ]
        res = ""
        for symbol, val in reversed(sym):
            cnt = num//val
            res += cnt * symbol
            num = num % val
        return res


x = solution()
print(x.intToRoman(1994))
