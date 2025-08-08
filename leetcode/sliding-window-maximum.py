from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        d = deque()
        result = []
        l = 0
        for r in range(len(nums)):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)
            if d[0] < l:
                d.popleft()
            if r >= k-1:
                result.append(nums[d[0]])
                l+=1  
        return result


