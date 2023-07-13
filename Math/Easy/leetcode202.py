class solution:
    def isHappy(self, n: int):
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    def sumOfSquares(self, x):
        S = 0
        while x:
            S += (x % 10) ** 2
            x //= 10
        return S


x = solution()
print(x.isHappy(19))
