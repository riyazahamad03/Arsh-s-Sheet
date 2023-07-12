class solution:
    def reverse(self, x: int):
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        if rev < - 2**31 or rev > 2**31 - 1:
            return 0
        return sign * rev


x = solution()
print(x.reverse(123))
