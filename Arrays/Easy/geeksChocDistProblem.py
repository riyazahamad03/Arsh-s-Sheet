class solution:
    def findMinDiff(self, arr: list[int], n: int, m: int):
        if m == 0 or n == 0:
            return 0
        arr.sort()

        if n < m:
            return -1

        minDiff = arr[m - 1] - arr[0]

        for idx in range(len(arr) - m + 1):
            minDiff = min(minDiff, arr[idx + m - 1] - arr[idx])

        return minDiff


x = solution()
arr = [12, 4, 7, 9, 2, 23, 25, 41,
       30, 40, 28, 42, 30, 44, 48,
       43, 50]
print(x.findMinDiff(arr, len(arr), 7))
