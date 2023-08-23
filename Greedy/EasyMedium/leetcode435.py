class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        count = 0
        prevEnd = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                count+=1
                prevEnd = min(prevEnd,intervals[i][1])
        return count


x = Solution()
print(x.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))