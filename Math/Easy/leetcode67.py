class solution:
    def addBinary(self, a: str, b: str):
        res, carry = "", 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digA = ord(a[i]) - ord("0") if i < len(a) else 0
            digB = ord(b[i]) - ord("0") if i < len(b) else 0

            tot = digA + digB + carry
            char = str(tot % 2)
            res = char + res
            carry = tot//2
        if carry:
            res = "1" + res
        return res


x = solution()
print(x.addBinary(a="11", b="1"))
