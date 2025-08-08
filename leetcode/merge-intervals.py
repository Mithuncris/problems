class Solution:
    def merge(self, intervals):
        intervals.sort()
        prev = None
        res = []
        for s, e in intervals:
            if prev is None:
                start = s
                prev = e
                continue
            if prev>=s:
                prev = max(e, prev)
            else:
                res.append([start, prev])
                start = s
                prev = e
        res.append([start, prev])
        return res