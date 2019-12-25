class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort()
        nlen = len(intervals)
        i = 0
        while i < nlen - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                left = intervals[i][0]
                right = max(intervals[i][1], intervals[i + 1][1])
                intervals[i] = [left, right]
                intervals.pop(i + 1)
                nlen -= 1
                continue
            i += 1
        return intervals


slu = Solution()
print(slu.merge([[1,4],[0,2],[3,5]]))
