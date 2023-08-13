class Solution:
    def maxLen(self, n, arr):

        isSeen = {}
        prefix_sum = 0
        max_length = 0

        for i in range(n):
            prefix_sum += arr[i]

            if prefix_sum == 0:
                max_length = i + 1

            if prefix_sum in isSeen:
                max_length = max(max_length, i - isSeen[prefix_sum])
            else:
                isSeen[prefix_sum] = i

        return max_length


x = Solution()
print(x.maxLen(8 , [15, -2, 2, -8, 1, 7, 10, 23]))
