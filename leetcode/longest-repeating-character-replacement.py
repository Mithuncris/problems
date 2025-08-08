from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        m = float('-inf')
        maxf = float('-inf')

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            while (r-l+1) - maxf > k :
                count[s[l]] -= 1
                l+=1
            m = max(m, (r-l+1))
        return m
            