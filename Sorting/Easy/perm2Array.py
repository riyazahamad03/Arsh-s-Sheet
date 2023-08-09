class solution:
    def permuteTwoArray(self, a: list[int], b: list[int], k: int):
        a.sort()
        b.sort(reverse=True)

        for i in range(len(a)):
            if a[i] + b[i] < k:
                return False

        return True


x = solution()
print(x.permuteTwoArray([2, 1, 3], [7, 8, 9], 10))
