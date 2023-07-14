class solution:
    def isPowerOfTwo(self, n: int):
        if n == 1:
            return True

        if n % 2 == 0:
            return self.isPowerOfTwo(n//2)
        else:
            return False


class solution2:
    def isPowerofTwo(self, n: int):
        if n > 0:
            return n & (n - 1) == 0


# this solution will result in runTimeError
x = solution()
print(x.isPowerOfTwo(3))

x = solution2()
print(x.isPowerofTwo(3))
