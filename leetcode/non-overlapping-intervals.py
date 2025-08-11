class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key= lambda x:x[1])
        print(intervals)
        prev = float('-inf')
        ans = 0
        for s, e in intervals:
            if prev>s:
                ans += 1
            else:
                prev = e
        return ans