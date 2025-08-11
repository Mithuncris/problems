class Solution:
    def triangleNumber(self, nums) -> int:
        nums.sort()
        ans = 0
        for i in range(2, len(nums)):
            l = 0
            r = i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    ans += (r-l)
                    r-=1
                    continue
                l+=1
        return ans