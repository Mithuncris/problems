from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums, k: int) -> int:
        count = defaultdict(int)
        curr = 0
        l = 0
        m = float('-inf')
        for r in range(len(nums)):
            curr += nums[r]
            count[nums[r]] += 1
            if (r-l+1) > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                curr -= nums[l]
                l+=1
            if len(count) == k == (r-l+1):
                m = max(m, curr)
        return m if m!=float('-inf') else 0