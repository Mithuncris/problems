class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        nums.sort()
        l = 0
        ans = float('inf')
        for r in range(k-1,len(nums)):
            ans = min (ans, nums[r]-nums[l])
            l+=1
        return ans