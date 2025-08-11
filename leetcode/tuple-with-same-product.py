class Solution:
    def tupleSameProduct(self, nums) -> int:
        pairs = {}
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = nums[i]*nums[j]
                pairs[prod] = pairs.get(prod,0)+1
                ans += 8*(pairs[prod]-1)
        return ans