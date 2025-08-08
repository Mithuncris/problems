class Solution:
    def longestSubarray(self, nums):
        zero = 0
        total = 0
        l = 0
        m = float('-inf')
        for r in range(len(nums)):
            if nums[r]==0:
                total += 1
            while total>1:
                if nums[l]==0:
                    total -= 1
                l+=1
            m = max(m, (r-l))
        return m if m!=float('-inf') else 0