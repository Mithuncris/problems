class Solution:
    def longestOnes(self, nums, k):
        l = 0 
        zeroes = 0
        m = float('-inf')
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[l]==0:
                    zeroes -= 1
                l+=1
            m = max(m, (r-l+1))
        return m