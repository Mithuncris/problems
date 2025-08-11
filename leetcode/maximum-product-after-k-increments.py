import heapq
class Solution:
    def maximumProduct(self, nums, k: int) -> int:
        h = []
        for i in nums:
            heapq.heappush(h, i)
        for _ in range(k):
            heapq.heappush(h, heapq.heappop(h)+1)
        ans = 1
        for i in h:
            ans *= i
        return ans % (1000000007)