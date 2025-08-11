class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        if not cardPoints:
            return 0
        n = len(cardPoints)
        total = sum(cardPoints)
        for i in range(n-k):
            total -= cardPoints[i]
        l = 0
        r = n-k
        m = total
        for i in range(k):
            total += cardPoints[l]
            l+=1
            total -= cardPoints[r]
            r+=1
            m = max(m, total)
        return m