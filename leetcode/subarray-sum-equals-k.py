class Solution:
    def subarraySum(self, nums, k: int) -> int:
        v = {}
        v[0] = 1
        prefix = 0
        ans  = 0
        for i in nums:
            prefix += i
            if prefix-k in v:
                ans += v[prefix-k]
            v[prefix] = v.get(prefix, 0)+1
        return ans