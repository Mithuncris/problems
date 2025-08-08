class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        m = float('-inf')
        l = 0
        for r in range(len(s)):
            while l<r and s[r] in d:
                d.remove(s[l])
                l+=1
            d.add(s[r])
            m = max(m, (r-l+1))
        return m if m!=float('-inf') else 0