class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-1):
            nRow = [1] * n
            for j in range(n-2, -1, -1):
                nRow[j] = nRow[j+1] + row[j]
            row = nRow
        return row[0]


x = Solution()
print(x.uniquePaths(m=3, n=7))
