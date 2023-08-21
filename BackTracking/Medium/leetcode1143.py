class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        d = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    d[i][j] = 1 + d[i+1][j+1]
                else:
                    d[i][j] = max(d[i+1][j], d[i][j+1])
        return d[0][0]


x = Solution()
print(x.longestCommonSubsequence(text1="abcde", text2="ace"))
