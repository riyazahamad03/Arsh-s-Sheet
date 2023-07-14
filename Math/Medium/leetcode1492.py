import math


class solution:
    def kthFactor(self, n: int, k: int):
        c = 0
        for i in range(1, n + 1):
            if not n % i:
                c += 1
            if c == k:
                return i
        return -1

    def kthFactor2(self, n: int, k: int):
        big, small = [], []
        for num in range(1, int(math.sqrt(n)) + 1):
            if not n % num:
                if num == n//num:
                    small.append(num)
                else:
                    small.append(min(num, n//num))
                    big.append(max(num, n//num))
        big.reverse()
        res = small + big
        if len(res) >= k:
            return res[k - 1]
        return -1


x = solution()
print(x.kthFactor(n=12, k=3))
print(x.kthFactor2(n=12, k=3))
