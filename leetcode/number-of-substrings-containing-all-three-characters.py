class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {i:0 for i in 'abc'}
        l = 0
        ans = 0
        for r in range(len(s)):
            d[s[r]] += 1
            while d['a']!=0 and d['b']!=0 and d['c']!=0:
                d[s[l]] -= 1
                l+=1
            ans += l
        return ans 