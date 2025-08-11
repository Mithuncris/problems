class Solution:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        prefix = 0
        v = {}
        v[0] = 1
        ans = 0
        for i in nums:
            prefix += i
            if prefix-goal in v:
                ans += v[prefix-goal]
            v[prefix] = v.get(prefix, 0)+1
        return ans