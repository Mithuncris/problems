from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p)>len(s): return []
        res = []
        ds = defaultdict(int) 
        dp = defaultdict(int) 
        for i in range(len(p)):
            dp[p[i]] += 1
            ds[s[i]] += 1
        l = 0
        if ds==dp:
            res.append(l)
        for r in range(len(p), len(s)):
            ds[s[r]]+=1
            ds[s[l]] -= 1
            if ds[s[l]] == 0:
                del ds[s[l]]
            l+=1
            if ds==dp:
                res.append(l)
        return res 