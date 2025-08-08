from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        count = defaultdict(int)
        for i in t:
            count[i] += 1
        window = defaultdict(int)
        have = 0
        need = len(count)
        l = 0
        m = float('inf')
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            while have==need:
                if s[l] in count and count[s[l]]>=window[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                if (r-l+1)<m:
                    m = (r-l+1)
                    res = [l, r]
                l+=1
        return s[res[0]:res[1]+1]

            