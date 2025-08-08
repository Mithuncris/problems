from collections import defaultdict
class Solution:
    def totalFruit(self, fruits):
        l = 0
        m = float('-inf')
        d = defaultdict(int)
        for r in range(len(fruits)):
            d[fruits[r]] += 1
            while len(d)>2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l+=1
            m = max(m, (r-l+1))
        return m
            