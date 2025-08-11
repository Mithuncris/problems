from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        d = deque()
        d.append((0,0))
        visited = set()
        visited.add((0,0))
        while d:
            wx, wy = d.popleft()
            if wx==target or wy==target or wx+wy == target:
                return True
            
            next = set()
            next.add((wx, 0))
            next.add((0, wy))
            next.add((x, wy))
            next.add((wx, y))
            amount = min(wx, y-wy)
            next.add((wx-amount, wy+amount))
            amount = min(x-wx, wy)
            next.add((wx+amount, wy-amount))
            for state in next:
                if state not in visited:
                    d.append(state)
                    visited.add(state)
        return False